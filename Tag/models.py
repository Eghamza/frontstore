from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class tag(models.Model):
    label = models.CharField(max_length=255)

class taggedItem(models.Model):
    tag = models.ForeignKey(tag,on_delete=models.CASCADE)
    #tagged item object
    contant_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    
    #object_ID
    object_ID = models.PositiveSmallIntegerField()
    #contat object
    contant_object = GenericForeignKey('contant_type','object_ID')



