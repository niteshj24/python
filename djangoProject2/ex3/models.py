from django.db import models

class routerapi(models.Model):
    sapid = models.CharField(max_length=18)
    hostname = models.CharField(max_length=14)
    loopback = models.CharField( primary_key=True , max_length=15)
    macip = models.CharField(max_length=17)
    is_delete = models.PositiveSmallIntegerField(default=0)