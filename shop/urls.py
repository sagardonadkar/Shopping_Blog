from django.contrib import admin
from django.urls import path, include
from shop import  views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name = "home"),
    path('about/', views.index, name = "home"),
    path('contact/', views.contact, name = "contact"),
    path('tracker/', views.tracker, name = "tracker"),
    path('search/', views.search, name = "search"),
    path('productview/', views.product_view, name = "productview"),
    path('checkout', views.checkout, name = "checkout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)