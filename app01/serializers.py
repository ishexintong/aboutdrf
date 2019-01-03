
from rest_framework.serializers import ModelSerializer,CharField,HyperlinkedModelSerializer,HyperlinkedIdentityField
from rest_framework.validators import  ValidationError
from app01.models import *

#文章的序列化
class ArticleModelSerializer(ModelSerializer):
    type_str=CharField(source='get_type_display',read_only=True)   #只是做取数据展示，当post请求时候不做数据的校验
    class Meta:
        model=Article #绑定的是哪一个ORM类
        fields="__all__"   #['id','title','type']
        depth=1            #官方推荐不超过10层

#文章超级链接序列化
class ArticleHyperLinkedSerializer(HyperlinkedModelSerializer):
    school=HyperlinkedIdentityField(view_name='school_detail',lookup_url_kwarg='id')
    class Meta:
        model=Article  #绑定的是哪一个ORM类
        fields=['id','title','school']

#学校的序列化
class SchoolModelSerializer(ModelSerializer):

    class Meta:
        model=School
        fields='__all__'

#Tag的序列化
class TagModelSerializer(ModelSerializer):

    class Meta:
        model=Tag
        fields="__all__"

#评论的序列化
class CommentModelSerializer(ModelSerializer):
    #用于校验的钩子函数 类似Form中的clean
    def validate_content(self,value):
        if '曹' in value:
            raise ValidationError('不符合社会主义核心价值观')
        else:
            return value

    #全局的校验的钩子函数
    # def validate(self, attrs):
    #     self.validated_data #经过校验的数据 ，类似Form中的cleaned_data
    class Meta:
        model=Comment
        fields='__all__'
        #定义额外的参数
        extra_kwargs={
            'content':{
                'error_messages':{
                    'required':'内容不能为空',
                }
            },
            'article':{
                'error_messages':{
                    'required':'文章不能为空'
                }
            }
        }