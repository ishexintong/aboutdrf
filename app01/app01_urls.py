from app01 import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
urlpatterns = [
    url(r'article/$', views.Article.as_view()),
    url(r'school/(?P<id>\d+)',views.School.as_view(),name='school_detail'),
    # url(r'comment/',views.Comment.as_view(),name='comment'),

]

router=DefaultRouter()
router.register(r'comment',views.CommentViewSet)
urlpatterns+=router.urls