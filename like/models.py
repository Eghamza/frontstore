from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class likeItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Content_Type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_ID = models.PositiveSmallIntegerField()
    Content_object = GenericForeignKey('Content_Type','object_ID')
