from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_all = Phone.objects.all()
    context = {'phones': phone_all}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter().first()
    context = {'phones': phone}
    return render(request, template, context)
