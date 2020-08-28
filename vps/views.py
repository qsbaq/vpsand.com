from django.shortcuts import render
from vps.models import Goods,Subscribe,Passwd
from django.contrib import admin
from django.http import HttpResponse
import json,hashlib
from django.contrib.auth.decorators import login_required
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
    

def tools(request):
    return render(request,'tools.html',{})




@login_required
def encrypt(request):
    input_str = request.GET.get('input_str')
    method = request.GET.get('type')
    if method == 'MD5' :
        output = md5(input_str)

        try :
            Passwd.objects.add(strings=input_str,md5=output)
        except:
            pass

    return HttpResponse(output)








def md5(jstr):
    hl = hashlib.md5()
    hl.update(jstr.encode('utf-8'))
    return hl.hexdigest()
