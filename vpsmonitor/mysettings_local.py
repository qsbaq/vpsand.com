
'''
邮箱配置文件
'''
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.163.com'  # 如果是 163 改成 smtp.163.com
EMAIL_PORT = 465
EMAIL_HOST_USER = 'laoji_org@163.com' # 帐号
EMAIL_HOST_PASSWORD = '邮箱密码'  # 密码
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER