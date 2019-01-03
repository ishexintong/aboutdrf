from django.db import models

# Create your models here.
#文章表
class Article(models.Model):
    title=models.CharField(max_length=32,unique=True,error_messages={'unique':'文章标题不能为空'})
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    type=models.IntegerField(choices=((1,'原创'),(2,'转载')),default=1)
    school=models.ForeignKey(to='School',on_delete=models.CASCADE)
    tag=models.ManyToManyField(to='Tag')
#文章来源表
class School(models.Model):
    name=models.CharField(max_length=32)
#文章标签表
class Tag(models.Model):
    name=models.CharField(max_length=32)

#文章评论表
class Comment(models.Model):
    content=models.TextField()
    article=models.ForeignKey(to='Article',on_delete=models.CASCADE)

#用户信息表
class UserInfo(models.Model):
    username=models.CharField(max_length=32)
