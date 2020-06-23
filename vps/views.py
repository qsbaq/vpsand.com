from django.shortcuts import render
from vps.models import Company ,Goods
from django.http import JsonResponse

from django.core import serializers
import json
# Create your views here.


def index(request):
    goods = Goods.objects.all().values('pid','company','dc',"cpu",'ram','disk','bandwidth','traffic','route','ipv4','arch','annual','quarter','month','stock','company__name','company__url')
    lastObj = Goods.objects.values('update_time').last()
    update_time = lastObj['update_time'].strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'index.html', {'goods': json.dumps(list(goods)) ,'update_time':update_time })
