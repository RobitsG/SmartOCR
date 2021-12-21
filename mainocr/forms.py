from django import forms
from django.db.models import fields
from .models import Image

class ImageForm(forms.Form):
    class Meta:
        model = Image
        fields = ('img')