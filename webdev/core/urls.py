from django.urls import path
from . import views

urlpatterns = [
    path('nivana/', views.nivana_index, name='nivana_index'),
]
