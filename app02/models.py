from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
# Create your models here.
class Course(models.Model):
    '''
    专题课
    '''
    name = models.CharField(max_length=32,verbose_name='课程名')
    #不影响数据库中的列，只为了加速数据的查询
    price_polict_list=GenericRelation('PricePolicy')
    def __str__(self):
        return self.name

class DegreeCourse(models.Model):
    '''
    学位课
    '''
    name=models.CharField(max_length=32)

class PricePolicy(models.Model):
    '''
    价格策略
    '''
    price=models.PositiveIntegerField(verbose_name='价格')
    period=models.IntegerField(verbose_name='周期')
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE,verbose_name='表的id')
    object_id=models.PositiveIntegerField(verbose_name='列的id')
    #不影响数据库的列，用于帮助开发者增加或者查询数据
    content_object=GenericForeignKey('content_type','object_id')
    def __str__(self):
        return str(self.price)