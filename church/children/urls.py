from django.conf.urls import url
from . import views

app_name = 'children'

urlpatterns = [
    url(r'^$', views.children_ministry, name='child'),
]
