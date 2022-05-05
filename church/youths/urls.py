from django.conf.urls import url
from . import views

app_name = 'youths'

urlpatterns = [
    url(r'^$', views.youth_ministry, name='youth'),
]
