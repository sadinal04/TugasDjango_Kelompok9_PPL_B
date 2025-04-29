from django.http import HttpResponse
from django.shortcuts import render

# Data produk contoh
produk_list = {
    1: {
        'nama': 'Sound System X200',
        'deskripsi': 'Sound system berkualitas tinggi dengan bass yang dalam dan suara jernih, cocok untuk acara indoor maupun outdoor.'
    },
    2: {
        'nama': 'Gamepad Pro GX1',
        'deskripsi': 'Gamepad ergonomis dengan koneksi wireless, respons cepat, dan kompatibel untuk PC dan konsol gaming.'
    },
    3: {
        'nama': 'Mouse Gaming UltraSpeed',
        'deskripsi': 'Mouse gaming presisi tinggi dengan 6 tombol programable, lampu RGB, dan sensor DPI hingga 16000.'
    },
}


def home(request):
    return render(request, 'produk/home.html')

def daftar_produk(request):
    context = {'produk_list': produk_list}
    return render(request, 'produk/daftar_produk.html', context)

def detail_produk(request, id):
    produk = produk_list.get(id)
    if not produk:
        return HttpResponse("<h1>Produk tidak ditemukan</h1>")
    context = {'produk': produk}
    return render(request, 'produk/detail_produk.html', context)

def kontak(request):
    return render(request, 'produk/kontak.html')
