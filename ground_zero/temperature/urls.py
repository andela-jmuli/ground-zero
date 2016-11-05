from django.conf.urls import url, include

from temperature import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.get_temperature, name='get_temp'),
]
