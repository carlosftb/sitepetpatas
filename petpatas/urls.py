from django.urls import path
from petpatas.views import index

urlpatterns = [
    path('', index),

]