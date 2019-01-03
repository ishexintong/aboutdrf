import os
import random
if __name__ == '__main__':
    ''''
    在一个py文件中使用django的环境变量
    '''
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aboutdrf.settings")
    import django
    django.setup()
    article_list=[]
    from app01 import models
    for item in range(20):
        title='python学习之三年用不上%'+str(item)
        school_id=random.randint(1,3)
        #tag=random.randint(1,4)
        type=random.randint(1,2)
        temp=models.Article(title=title,school_id=school_id,type=type)
        article_list.append(temp)
    models.Article.objects.bulk_create(article_list)
    #models.Article.objects.create(title='python学习之三年用不上',school_id=1,)