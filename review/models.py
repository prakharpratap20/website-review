from django.db import models


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    site_url = models.CharField(max_length=1000)
    site_image_url = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=1000000, default=None, null=True)
