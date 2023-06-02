from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('news', Posts.as_view(), name='news'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('dogs', Dogs.as_view(), name='dogs'),
    #path('post/<str:slug>', GetPost.as_view(), name='news'),
    path('dog/<str:slug>', GetDog.as_view(), name='dog'),
    path('post/<str:slug>', GetPost.as_view(), name='post'),
    path('receipt', receipt, name='receipt'),
    path('photos', PhotosGallery.as_view(), name='photos'),
    path('achivements', achivements, name='achivements')
]