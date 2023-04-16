from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio', views.portfo, name='portfolio'),
    path('contact', views.contacts, name='contact'),
    path('skills', views.skill, name='skills'),
]