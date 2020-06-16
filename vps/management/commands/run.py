#!/usr/bin/env python
# coding: utf-8
from django.core.management.base import BaseCommand, CommandError
from vps.models import Company ,Goods
from urllib import request
import time
# from vps.models import Goods
import sys,threading
class Command(BaseCommand):
    def handle(self, *args, **options):
        goodsObj = Goods.objects.all()
        for g in goodsObj:
            t = threading.Thread(target=self.updateStock, args=(g,))
            t.start()

    def updateStock(self,good):
        url = good.company.url + str(good.pid)
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        try:
            req=request.Request(url,headers=header)
            page=request.urlopen(req,timeout=2).read()
            status = '200'
            if str(page).find(good.company.out_of_stock_string) > 0 :
                stock = 0    
            else:
                stock = 1

            good.stock = stock
            good.save()  

        except :
            status = 'TimeOut'
            stock = 'Unknown'

        print(time.strftime('%Y-%m-%d %H:%M:%S')+' -- '+url + ' -- ' + str(status) +' -- '+ str(stock))