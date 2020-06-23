from django.db import models

# Create your models here.
booleanChoices = ((0,"否"),(1,"是"))

class Company(models.Model):
    name = models.CharField('商家名称', max_length=256, unique=True)
    url = models.CharField('网址', max_length=256 , help_text='https://bwh88.net/aff.php?aff=991&pid=')
    need_monitor = models.BooleanField(verbose_name='是否需要监控',choices=booleanChoices,default=1)
    out_of_stock_string = models.CharField('缺货字符串',max_length=256,default='Out of Stock') 
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'company'        
        verbose_name = '商家信息'
        verbose_name_plural = '商家信息'


class Goods(models.Model):
    archChoices = (
        ('KVM','KVM'),
        ('OpenVZ','OpenVZ')
    )
    stockChoices = (
        (0,'无货'),
        (1,'有货')        
    )
    lineChoices = (
        ('CN2-GT','CN2-GT'),
        ('CN2-GIA','CN2-GIA'),
        ('BGP','BGP'),
        ('PCCW','PCCW'),
    )
    dcChoices = (
        ('ATL','ATL'),
        ('LA','LA'),
        ('SEA','SEA'),
        ('HK','HK'),
        ('Taiwan','Taiwan'),
        ('Frankfurt','Frankfurt'),
    )
    company = models.ForeignKey(Company , to_field='id' , on_delete=models.DO_NOTHING , verbose_name="商家",blank=False,null=False)
    pid = models.IntegerField(verbose_name='PID',blank=False,null=False )
    dc = models.CharField('机房位置', max_length=256,choices=dcChoices)
    cpu = models.IntegerField('CPU', default=1)
    ram = models.CharField('内存', max_length=256)
    disk = models.CharField('硬盘', max_length=256)
    bandwidth = models.CharField('带宽', max_length=256)
    traffic = models.CharField('流量', max_length=256)
    route = models.CharField('线路', max_length=256,choices=lineChoices)
    ipv4 = models.IntegerField('IPV4',default=1)
    arch = models.CharField('架构', max_length=256,choices=archChoices,default='KVM')
    annual = models.CharField('年付', max_length=256,)
    quarter = models.CharField('季付', max_length=256,blank=True,null=True)
    month = models.CharField('月付', max_length=256,blank=True,null=True)
    stock = models.IntegerField( choices=stockChoices,verbose_name='库存' , default=0 )
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'PID：{} - 年付：${}'.format(self.pid,self.annual)

    class Meta:
        managed = True
        db_table = 'goods'
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'

