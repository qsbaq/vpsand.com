#!/usr/bin/env python
# coding: utf-8
'''
运行方法：
python .\manage.py run
'''
from django.core.management.base import BaseCommand, CommandError
from vps.models import Company ,Goods
import requests
import time
# from vps.models import Goods
import sys,threading
lock = threading.Semaphore(12)
class Command(BaseCommand):
    def handle(self, *args, **options):
        goodsObj = Goods.objects.filter(company__need_monitor = 1 )
        
        for g in goodsObj:
            t = threading.Thread(target=self.updateStock, args=(g,))
            t.start()

    def updateStock(self,good):
        lock.acquire()	#计数器获得锁
        url = good.company.url + str(good.pid)
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        try:
            res=requests.get(url,headers=header,timeout=2)
            res.encoding='utf-8'
            status = res.status_code
            if status != 200 :
                raise Exception(status)
            else :
                if str(res.text).find(good.company.out_of_stock_string) > 0 :
                    stock = 0    
                else:
                    stock = 1

                good.stock = stock
                good.save()  

        except Exception as e :
            status = e
            stock = 'Unknown'

        print(time.strftime('%Y-%m-%d %H:%M:%S')+' -- '+ url + ' -- ' + str(status) +' -- '+ str(stock))
        lock.release()	#计数器释放锁