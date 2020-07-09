from django.shortcuts import render
from vps.models import Goods,Subscribe
from django.contrib import admin
from django.http import HttpResponse
import json
# Create your views here.


def index(request):
    goods = Goods.objects.all().values('pid',
                                        'company',
                                        'dc',
                                        "cpu",'ram',
                                        'disk',
                                        'bandwidth',
                                        'traffic',
                                        'route',
                                        'ipv4',
                                        'arch','annual',
                                        'quarter',
                                        'month','stock',
                                        'company__name',
                                        'company__url',
                                        'company__connect_pid',
                                        'company__need_monitor',
                                        'sort'
            ).order_by('-sort')
    lastObj = Goods.objects.values('update_time').filter(company__need_monitor = 1).last()
    update_time = lastObj['update_time'].strftime("%Y-%m-%d %H:%M:%S") if lastObj else None
    return render(request, 'index.html', {'goods': json.dumps(list(goods)) ,
                                            'update_time':update_time,
                                            'title':admin.site.site_header ,
    })


def subscribe(request):
    try:
        Subscribe.objects.create(email = request.GET.get('email'))
    except :
        pass
    return HttpResponse('1')
    

