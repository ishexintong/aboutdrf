from django.shortcuts import render,HttpResponse
from  django.views import View
from app02 import models
# Create your views here.

class AIndex(View):

    def get(self,request):
        #插入课程表
        #models.Course.objects.bulk_create([models.Course(name='21天入门到放弃'),models.Course(name='丛删库到跑路'),models.Course(name='24小时转c++'),models.Course(name='数据结构')])
        #models.DegreeCourse.objects.bulk_create([models.DegreeCourse(name='Python全栈'),models.DegreeCourse(name='JavaSe编程'),models.DegreeCourse(name='BigData的应用'),models.DegreeCourse(name='人工智能')])

        #Course插入价格策略
        # obj=models.Course.objects.filter(name='21天入门到放弃').first()
        # models.PricePolicy.objects.create(price=9,period=30,content_type_id=12,object_id=obj.id)
        # models.PricePolicy.objects.create(price=19,period=90,content_type_id=12,object_id=obj.id)
        # models.PricePolicy.objects.create(price=29,period=120,content_type_id=12,object_id=obj.id)

        # #DegreeCourse插入价格策略
        # obj2=models.DegreeCourse.objects.filter(name='Python全栈').first()
        # models.PricePolicy.objects.create(price=199,period=30,content_type_id=13,object_id=obj2.id)
        # models.PricePolicy.objects.create(price=299,period=60,content_type_id=13,object_id=obj2.id)
        # models.PricePolicy.objects.create(price=599,period=90,content_type_id=13,object_id=obj2.id)

        #查询专题课id为1的所有的价格策略
        '''
        tc_obj=models.Course.objects.filter(id=1).first()
        price_list=models.PricePolicy.objects.filter(content_type__model='course',object_id=tc_obj.id)
        print(price_list)
        '''

        #查询所有的价格显示课程名称
        '''
        用到了model 中的 新增的辅助项 content_object=GenericForeignKey('content_type','object_id')
        price_list=models.PricePolicy.objects.all()
        for item in price_list:
            print(item.price,item.period,item.content_object.name,)
        '''

        #显示专题课程列表，并打印课程的价格信息
        course_list=models.Course.objects.all()
        for row in course_list:
            print(row.id,row.name)
            price_all=row.price_polict_list.all()
            for p in price_all:
                print('----------->',p.price,p.period)
        return HttpResponse('index')
