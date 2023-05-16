from django.db import models

class Thumbnail(models.Model):
    image_url = models.CharField(max_length=200)
    is_chosen = models.BooleanField(default=False)
