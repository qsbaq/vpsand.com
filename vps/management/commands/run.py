#!/usr/bin/env python
# coding: utf-8
'''
运行方法：
python .\manage.py run
'''
from vps.views import subscribe
from django.core.management.base import BaseCommand, CommandError
from vps.models import Goods,Subscribe
import requests , time
import threading
from django.core.mail import send_mail, send_mass_mail
import vpsmonitor.settings as settings

lock = threading.Semaphore(12)

class Command(BaseCommand):
    def handle(self, *args, **options):
        goodsObj = Goods.objects.filter(company__need_monitor = 1 )
        mail_list = list(Subscribe.objects.values('email'))
        mails = []
        for i in mail_list :
            mails.append(i['email'])

        for g in goodsObj:
            t = threading.Thread(target=self.updateStock, args=(g,mails))
            t.start()

    def updateStock(self,goodsObj,mails):
        lock.acquire()	#计数器获得锁
        url = goodsObj.company.url + str(goodsObj.pid)
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        try:
            res=requests.get(url,headers=header,timeout=2)
            res.encoding='utf-8'
            status = res.status_code
            if status != 200 :
                raise Exception(status)
            else :
                if str(res.text).find(goodsObj.company.out_of_stock_string) > 0 :
                    stock = 0    
                else:
                    stock = 1

                if( goodsObj.stock == 0 and stock == 1):
                    msg = '<a href="{}">{}</a>'.format( url,goodsObj.company.name+' '+
                                                        goodsObj.dc+' '+
                                                        str(goodsObj.cpu)+' '+
                                                        goodsObj.ram+' '+
                                                        goodsObj.disk+' '+
                                                        goodsObj.bandwidth+' '+
                                                        str(goodsObj.ipv4)+' '+
                                                        goodsObj.arch
                                                )
                    send_mail(
                        subject = '{} 上新啦_VPSAND.COM'.format(goodsObj.company.name),
                        message = msg,
                        from_email = settings.DEFAULT_FROM_EMAIL, 
                        recipient_list = mails
                    )

                goodsObj.stock = stock
                goodsObj.save()  
                
        except requests.exceptions.Timeout as e:
            status = 'TimeOut'
            stock = 'Unknown'

        except Exception as e :
            status = e
            stock = 'Unknown'

        print(time.strftime('%Y-%m-%d %H:%M:%S')+' -- '+ url + ' -- ' + str(status) +' -- '+ str(stock))
        lock.release()	#计数器释放锁