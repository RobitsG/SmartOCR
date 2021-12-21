import os
import shutil
import zipfile
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required

from .forms import ImageForm
from .models import Image
from .ocr import OCR
from .config import UPLOAD_PATH

# 删除缓存
def initialize():
    # 清空数据库
    Image.objects.all().delete()
    # 清除图片文件
    if os.path.exists(UPLOAD_PATH):
        shutil.rmtree(UPLOAD_PATH)

# 处理一张图片
def ocr_one(file, mode):
    img = Image.objects.create()
    img.img = file
    img.save()

    nMEDIA_ROOT = settings.MEDIA_ROOT.replace('\\',r'/')
    img_name = img.img.name
    img_path = nMEDIA_ROOT + r'/' + img_name
    text_url = img_name.split('.')[0] + '.txt'
    text_path = nMEDIA_ROOT + text_url
    print(text_path)

    # get OCR result
    text = OCR().getResult(img_path, mode=mode)['text']
    return img, text, text_url, text_path

@login_required(login_url='/userprofile/login/')
def get_ocr(request, mode):
    context = {'img_cleaned':'', 'text':'', 'text_url':'', 'flag':False, 'text_path_list':[], 'mode':mode}
    if request.method == 'POST':
        imageform = ImageForm(request.POST, request.FILES)
        if 'img' in request.FILES:
            if imageform.is_valid(): 
                initialize()
                img, text, text_url, _ = ocr_one(request.FILES['img'], mode=mode)
                context['img_cleaned'] = img
                context['text'] = text
                context['text_url'] = text_url
            else:
                context['text'] = "请上传正确的图片格式！"
                context['flag'] = True
        else: 
            context['text'] = "请重新选择图片！"
            context['flag'] = True
    elif request.method == 'GET':
        pass
    else:
        context['text'] = "请使用GET或POST请求数据"
        context['flag'] = True
    return render(request, 'mainocr/opennews.html', context)

@login_required(login_url='/userprofile/login/')
def multiple_ocr(request, mode):
    context = {'img_cleaned':'', 'text':'', 'text_url':'', 'flag':False, 'text_path_list':[], 'mode':mode}
    if request.method == 'POST':
        imageform = ImageForm(request.POST, request.FILES)
        if 'files' in request.FILES:
            if imageform.is_valid():
                initialize()
                text_path_list = []
                for file in request.FILES.getlist('files'):
                    _, _, _, text_path = ocr_one(file, mode=mode)
                    text_path_list.append(text_path)
                    context['text_path_list'] = text_path_list
            else:
                context['text'] = "请上传正确的图片格式！"
                context['flag'] = True
    elif request.method == 'GET':
        pass
    else:
        context['text'] = "请使用GET或POST请求数据"
        context['flag'] = True
    return render(request, 'mainocr/opennews.html', context)

def find_files(filepath):
    # find files
    path_list = [filepath]
    file_list = []
    while path_list:
        path = path_list.pop()
        for p in os.listdir(path):
            np = path + '/' + p
            if os.path.isdir(np):
                path_list.append(np)
            else:
                # only join txt files into filepath
                if np.split('.')[-1] == 'txt':
                    file_list.append(np)
    return file_list

def zip_files(file_list, zipfile_name='result.zip'):
    # zip files
    zipfile_path = os.path.join(os.path.join(UPLOAD_PATH, zipfile_name))
    with zipfile.ZipFile(zipfile_path, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_list:
            file_name = file.split('/')[-1]
            zf.write(file, arcname=file_name)
    return zipfile_path

@login_required(login_url='/userprofile/login/')
def download(request):
    if os.path.exists(UPLOAD_PATH):
        file_list = find_files(UPLOAD_PATH)
        if file_list:
            zipfile_path = zip_files(file_list)
            ziped_files = open(zipfile_path,'rb')
            response =FileResponse(ziped_files)
            response['Content-Type']='application/octet-stream'
            response['Content-Disposition']='attachment;filename="result.zip"'
            return response
    return render(request, 'alert.html', {'alert_text':"请先预测后再尝试下载！"})
