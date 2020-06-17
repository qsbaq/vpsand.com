from django.contrib import admin
from vps import models
from django.utils.html import format_html




# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'url','update_time')
    list_per_page = 20
    list_filter = ('name', )
    search_fields = ['name']
    list_display_links = ('name',)



class GoodsAdmin(admin.ModelAdmin):
    list_display = ('company', 'pid', 'ram','cpu','dc','disk','bandwidth','traffic','route','ipv4','arch','annual', 'stockStatus', 'update_time')
    list_per_page = 100
    # list_editable = ['companyId',]
    list_filter = ('company__name','dc','stock','arch' )
    # search_fields = ['companyId']
    ordering = ('company',)
    readonly_fields = ('stock', )
    list_display_links = ('company',)
    def stockStatus(self , obj):
        if obj.stock == 0:
            return format_html('<span style="color:red">{}</span>','无货')
        else:
            return format_html('<span style="color:green">{}</span>','有货')
    stockStatus.short_description = '库存'







admin.site.register(models.Company, CompanyAdmin)

admin.site.register(models.Goods, GoodsAdmin)


admin.site.site_header = 'VPS库存监控系统'
admin.site.site_title = 'VPS库存监控系统'
admin.site.index_title = '后台管理'