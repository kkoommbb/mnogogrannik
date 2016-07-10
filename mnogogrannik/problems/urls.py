from django.conf.urls import include,url

from . import views, models

urlpatterns = [
    # ex: /problems/
    url(r'^$', views.index, name='index'),
    # ex: /problems/5
    url(r'^(?P<problem_id>[0-9]+)/', views.single_problem, name='problem'),
]