from django.contrib import admin
from vps import models
from django.utils.html import format_html




# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'url','need_monitor','connect_pid','out_of_stock_string','update_time')
    list_per_page = 20
    list_filter = ('name','need_monitor' )
    search_fields = ['name']
    list_display_links = ('name',)



class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','company', 'pid', 'ram','cpu','dc','disk','bandwidth','traffic','route','ipv4','arch','annual', 'stockStatus','sort', 'update_time')
    list_per_page = 100
    # list_editable = ['is_topic',]
    list_filter = ('company__name','dc','stock','arch' )
    # search_fields = ['companyId']
    ordering = ('-sort','-id')
    # readonly_fields = ('stock', )
    # list_display_links = ('company',)
    def stockStatus(self , obj):
        if obj.stock == 0:
            return format_html('<span style="color:red">{}</span>','无货')
        else:
            return format_html('<span style="color:green">{}</span>','有货')
    stockStatus.short_description = '库存'


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id','email','status','update_time')
    search_fields = ['email',]




admin.site.register(models.Company, CompanyAdmin)

admin.site.register(models.Goods, GoodsAdmin)

admin.site.register(models.Subscribe, SubscribeAdmin)

admin.site.site_header = 'VPS库存监控系统'
admin.site.site_title = 'VPS库存监控系统'
admin.site.index_title = '后台管理'