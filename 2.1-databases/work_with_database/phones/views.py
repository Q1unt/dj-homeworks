from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    name_filter = request.GET.get('sort')
    if name_filter == 'name':
        tel = Phone.objects.order_by('name')
    if name_filter == 'min_price':
        tel = Phone.objects.order_by('price')
    if name_filter == 'max_price':
        tel = Phone.objects.order_by('-price')
    template = 'catalog.html'
    context = {'phones': tel}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter().first()
    context = {'phones': phone}
    return render(request, template, context)
