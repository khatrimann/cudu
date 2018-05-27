from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from . import views
app_name = 'cuduApp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^electronics', views.electronics, name='electronics')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)