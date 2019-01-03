from django.shortcuts import render
from rest_framework.views import  APIView
from  rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app01 import models
from app01 import serializers as app01_serializers
# Create your views here.

class Article(APIView):

    def get(self,request):
        res={'code':0}
        all_article=models.Article.objects.all()
        ser_obj=app01_serializers.ArticleHyperLinkedSerializer(all_article,many=True,context={'request':request})
        res['data']=ser_obj.data
        return Response(res)

class School(APIView):
    '''
    学校详情
    '''
    def get(self,request,id):
        res={'code':0}
        schoo_obj=models.School.objects.filter(pk=id).first()
        ser_obj=app01_serializers.SchoolModelSerializer(schoo_obj,context={'request':request})
        res['data']=ser_obj.data
        return Response(res)

class Comment(APIView):
    '''
    评论详情
    '''
    def get(self,request):
        res={'code':0}
        comment_obj=models.Comment.objects.all()
        ser_obj=app01_serializers.CommentModelSerializer(comment_obj,many=True)
        res['data']=ser_obj.data
        return Response(res)
    def post(self,request):
        pass

class CommentViewSet(ModelViewSet):
    ####套娃

    queryset = models.Comment.objects.all()
    serializer_class = app01_serializers.CommentModelSerializer

