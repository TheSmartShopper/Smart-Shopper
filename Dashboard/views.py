from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from ManageOffer.models import Offer
from ManageProduct.filter import ProductFilter
from ManageProduct.models import Product
from ManageStore.models import Store, Section, AD_imags


def Home(request):
    products = Product.objects.all()
    stores = Store.objects.all()
    section = Section.objects.all()
    offers = Offer.objects.all()
    myfilter = ProductFilter(request.GET, queryset=products)
    ads = AD_imags.objects.all()
    context = {
        'products': products,
        'Stores': stores,
        'offers': offers,
        'sections': section,
        'myfilter': myfilter,
        'ads': ads,
    }
    return render(request, 'Dashboard.html', context)


def section(request, sec):
    productsection = Product.objects.filter(product_sections=sec)
    myfilter = ProductFilter(request.GET, queryset=productsection)
    section = Section.objects.all()
    paginator = Paginator((productsection), 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'product': productsection,
        'sections': section,
        'page_obj': page_obj,
        'myfilter': myfilter
    }
    return render(request, 'HomePageSections.html', context)


def productsfilter(request):
    section = Section.objects.all()
    product = Product.objects.all()
    myfilter = ProductFilter(request.GET, queryset=product)
    products = myfilter.qs
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': products,
        'sections': section,
        'page_obj': page_obj,
        'myfilter': myfilter

    }
    return render(request, 'HomePageProduct.html', context)


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_500(request, exception):
    data = {}
    return render(request, '500.html', data)


def Maptest(request):
    loc = 'مركز البارحة القرآني، Irbid'
    context = {
        'loc': loc
    }
    return render(request, 'M.html', context)


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            ###########product #############
            lookupsproduct = Q(name__icontains=query) | Q(description__icontains=query) | Q(
                manufacturer__icontains=query) \
                             | Q(par_Code__icontains=query) | Q(product_sections__icontains=query) | Q(
                type__icontains=query)
            ########### store ##################
            lookupsstore = Q(name__icontains=query) | Q(description__icontains=query)
            # ############## offer ###################
            lookupsoffer = Q(name__icontains=query) | Q(products__name__icontains=query)

            #######################
            products = Product.objects.filter(lookupsproduct).distinct()
            stores = Store.objects.filter(lookupsstore).distinct()
            offers = Offer.objects.filter(lookupsoffer).distinct()
            myfilter = ProductFilter(request.GET, queryset=products)
            section = Section.objects.all()
            ads = AD_imags.objects.all()

            context = {
                'products': products,
                'Stores': stores,
                'offers': offers,
                'sections': section,
                'myfilter': myfilter,
                'ads': ads,
                'submitbutton': submitbutton}

            if not (products.count() + stores.count() + offers.count()) >= 1:
                messages.success(request, 'The ar no Match try  Another value')
                return redirect("Dashboard:Home")

            return render(request, 'Dashboard.html', context)

        else:
            return redirect("Dashboard:Home")

    return redirect("Dashboard:Home")
