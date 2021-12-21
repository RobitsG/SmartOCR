from django.db import models

class Image(models.Model):
    img = models.ImageField(upload_to='ocr/%Y%m%d/', blank=True)
