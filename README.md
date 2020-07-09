# VPS库存监控系统 vps-stock-monitor
本程序主要用户推荐VPS，并监控一些商家的库存。
项目主页：[https://www.jiloc.com/46825.html](https://www.jiloc.com/46825.html)

## 演示/Demo
[在线演示/Online Demo](https://vpsand.com)

## 安装/Install
本环境需要python3的运行环境以及python3-pip
下载源码后运行 `pip3 install django ; pip3 install requests`
然后将数据库导入
> python3 manage.py makemigrations --merge ; python3 manage.py migrate

## 创建后台超级用户
> python3 manage.py createsuperuser

## 开始启动服务
`python3 manage.py runserver 0.0.0.0:80`
启动后，在浏览器中打开 `http://127.0.0.1/admin` 的“商品”及“商家”中填入数据，否则首页无法运行。


## 配置邮件
将vpsmonitor/settings_local.py 重命名为 vpsmonitor/settings.py ，并设置好对应的邮箱信息。

## 定时监控/Crontab
定时每分钟检查VPS商家库存情况，需要在商家的属性中设定`检查库存`：`是`
然后将以下命令加入到crontab中。
> */1 * * * * cd /data/wwwroot/vps-stock-monitor/ ; python3 manage.py run > /dev/null 2>&1 &
