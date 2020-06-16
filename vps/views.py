from django.shortcuts import render
from vps.models import Company ,Goods
from django.http import JsonResponse

from django.core import serializers
import json
# Create your views here.


def index(request):
    goods = Goods.objects.all().values('company','dc',"cpu",'ram','disk','bandwidth','traffic','route','ipv4','arch','annual','stock','company__name')
    return render(request, 'index.html', {'goods': json.dumps(list(goods)) })
