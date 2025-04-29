from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                   # Homepage
    path('produk/', views.daftar_produk, name='produk'),  # Daftar produk
    path('produk/<int:id>/', views.detail_produk, name='detail_produk'),  # Detail produk
    path('kontak/', views.kontak, name='kontak'),         # Kontak
]
