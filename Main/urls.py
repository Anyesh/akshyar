from django.conf.urls import url
from . import views
app_name = "Main"
urlpatterns = [url(r'^$', views.index.as_view(), name='Home'), ]