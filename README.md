# 智能OCR项目实践

使用django编写的前端应用，需调用百度API

**Demo站：**http://madokacloud.top:8000/userprofile/login/

**本项目参考杜塞大佬的django个人博客项目，教程链接：**https://www.dusaiphoto.com/article/2/

#### 文件结构图

```
smartocr
│  db.sqlite3	#数据库文件
│  manage.py	#运行入口
│  ...
├─mainocr	#OCR主APP
│  │  ocr.py	#ocr模块
│  │  views.py	#response处理函数
│  │  ...  
│  └─migrations	#数据库生成中间文件             
├─media	#媒体文件
│  ├─avatar	#头像文件夹          
│  └─ocr	#图片及预测结果           
├─smartocr
│  settings.py	#设置
│  urls.py	#网址-函数 映射
│  ...          
├─static	#静态文件
│  └─bootstrap
│    ├─css 
│    └─js          
├─templates	#前端代码
│  │  alert.html
│  │  base.html
│  │  footer.html
│  │  header.html
│  ├─mainocr
│  │      opennews.html    
│  └─userprofile
│          edit.html
│          login.html
│          register.html         
└─userprofile	#用户APP
```

#### 环境要求

```
pip install -r requirements.txt
```

#### 下载与设置

git clone 下载：

```
git clone https://github.com/RobitsG/SmartOCR.git
```

打开 smartocr/smartocr/settings.py 文件末尾，按照注释编辑个人信息

```
# SMTP服务器，改为你的邮箱的smtp!
EMAIL_HOST = 'smtp.qq.com'
# 改为你自己的邮箱名！
EMAIL_HOST_USER = '######'
# 你的邮箱密码（QQ邮箱为特殊验证码）
EMAIL_HOST_PASSWORD = '######'
# 发送邮件的端口
EMAIL_PORT = 25
# 是否使用 TLS
EMAIL_USE_TLS = True
# 默认的发件人
DEFAULT_FROM_EMAIL = '###### <xxxxxx@qq.com>'
```

#### 运行方法

```
加载数据库：
python manage.py makemigrations
python manage.py migrate
创建超级管理员账户：
python manage.py createsuperuser
运行程序：
python manage.py runserver
```

接着访问 127.0.0.1:8000/userprofile/login/ 即可。