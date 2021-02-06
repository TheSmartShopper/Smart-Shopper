from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render

from ManageStore.forms import EditStoreForm, CreateStoreForm
from ManageStore.models import Store, AD_imags
from accounts.models import StoreAdminProfile


def view_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    products = store.products.all()
    ads = store.ADs.all()
    context = {
        'store': store,
        'products': products,
        'ads': ads,
    }
    return render(request, 'store.html', context)


def create_store(request):
    user = get_object_or_404(StoreAdminProfile, user=request.user)
    store_form = CreateStoreForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if store_form.is_valid():
            new_store = store_form.instance
            new_store.save()
            user.set_store(new_store.pk)
            return redirect('/')
    else:
        store_form = CreateStoreForm()
    context = {'form': store_form}
    return render(request, 'Create_Store.html', context)


def edit_store(request):
    user = get_object_or_404(StoreAdminProfile, user=request.user)
    store = get_object_or_404(Store, id=user.store.id)
    if request.method == 'POST':
        form = EditStoreForm(request.POST or None, request.FILES or None, instance=store)
        if form.is_valid():
            sec = form.cleaned_data.get('new_sections')
        if store.is_sections_exist(sec):
            messages.warning(request, 'This Section Is exist')
        elif str(sec) != '':
            store.add_sections(sec)
        else:
            store = form.instance
            store.save()
        return redirect('ManageStore:view_store', store.id)  # Redirect change
    else:
        form = EditStoreForm(instance=store)
    return render(request, 'edit_store.html', {'form': form})


def delete_ADs(request,ad_id):
    user = get_object_or_404(StoreAdminProfile, user=request.user)
    store = get_object_or_404(Store, id=user.store.id)
    ad= get_object_or_404(AD_imags ,id = ad_id)
    if request.method == 'POST':
        if store.ADs.get(id=ad.id):
            ad.delete()
            messages.warning(request, "AD Can't Delete  ")
        else:
            messages.warning(request,"AD Can't Delete  ")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_ADs(request):
    user = get_object_or_404(StoreAdminProfile, user=request.user)
    store = get_object_or_404(Store, id=user.store.id)

    if request.method == 'POST':
        new_AD = AD_imags()
        new_AD.name = store.name
        new_AD.ad_imags = request.FILES['ad_imags']
        new_AD.save()
        store.ADs.add(new_AD)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def products_in_section(request, store_id, section):
    store = get_object_or_404(Store, id=store_id)
    return store.products.filter(product_sections=section)
