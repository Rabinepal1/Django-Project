
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    path('news-details/<slug>', views.details, name='details'),
    path('category/<slug>', views.category_view, name='category')
]