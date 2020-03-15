from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('About', views.About, name='About'),
    path('Blog', views.Blog, name='Blog'),
    path('Contact', views.Contact, name='Contact'),
    path('Rooms', views.Rooms, name='Rooms'),
    path('elements', views.elements, name='elements'),
    path('Services', views.Services, name='Services'),
    path('Single_blog', views.Single_blog, name='Single_blog'),
    path('main', views.main, name='main'),
]