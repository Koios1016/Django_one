from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = "polls"
urlpatterns = [
    # path('', views.index),
    # # ex: /polls/
    # re_path(r'^$', views.index, name='index'),
    # # ex: /polls/5/
    # re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # 改用类视图
    # 第2,3条目中将原来的<question_id>修改成了<pk>
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
