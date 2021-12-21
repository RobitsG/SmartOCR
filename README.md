# 智能OCR项目实践

使用django编写的前端应用，需调用百度API

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

