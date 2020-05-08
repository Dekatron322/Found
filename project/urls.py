from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('causes/', views.causes, name="causes"),
    path('contact/', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('single-causes', views.single_causes, name="single-causes"),
    path('news', views.news, name="news")
]
