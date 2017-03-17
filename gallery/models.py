from django.db import models


class ImgList(models.Model):
    img_name = models.CharField(max_length=100)
    img_path = models.CharField(max_length=100)
