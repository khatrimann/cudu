from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^home/', views.index, name='index'),
    url(r'^electro/', views.shop1, name='electronics'),
]