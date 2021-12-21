# 引入path
from django.urls import path

from . import views

app_name = 'mainocr'

urlpatterns = [
    # hello world
    path('ocr/<int:mode>/', views.get_ocr, name='get_ocr'),
    path('multiple-ocr/<int:mode>/', views.multiple_ocr, name='multiple_ocr'),
    path('download/', views.download, name='download'),
]