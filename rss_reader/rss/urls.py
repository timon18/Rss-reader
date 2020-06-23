from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('saved/', views.saved, name='saved'),
]

urlpatterns += [
url(r'^signup/$', views.signup, name='signup'),
url(r'^tags/$', views.tags, name='tags'),
url(r'^save/$', views.save, name='save'),
url(r'^delete/$', views.delete, name='delete'),
]
