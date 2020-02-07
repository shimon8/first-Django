from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^(?P<album_id>[0-9]+)/$',views.detailes,name="detailes"),
    url(r'^(?P<album_id>[0-9]+)/favoraite$', views.favoraite, name="favoraite"),

]
