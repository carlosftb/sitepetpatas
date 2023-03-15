from django.urls import path
from petpatas.views import index, service, about, findus


urlpatterns = [
    path('', index, name='index'),
    path('service/', service, name='service'),
    path('about/', about, name='about'),
    path('findus/', findus, name='findus'),
    

]