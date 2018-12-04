from django.conf.urls import url
from . import views

app_name = 'researchably'

urlpatterns = [
    #/researchably/
    url(r'^$', views.home_page, name='index'),
    #/researchably/output/
    url(r'^output', views.output_page, name='output'),
]