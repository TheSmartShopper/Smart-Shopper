from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from ManageReview.forms import ReviewForm
from accounts.CustomerProfilemodel import CustomerProfile
from accounts.models import StoreAdminProfile
from .forms import ProductForm
from .models import Product


class ProductsCustomer():
    def add_to_favorite(request, id, ):
        user = get_object_or_404(CustomerProfile, user=request.user)
        product = get_object_or_404(Product, id=id)
        user.favorite.add(product)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def remove_to_favorite(request, id):
        user = get_object_or_404(CustomerProfile, user=request.user)
        p = Product.objects.get(id=id)
        user.favorite.remove(p)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ProductAdmin():

    def product_view(request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ReviewForm()
        return render(request, 'product_home.html', {'product': product, 'form': form})

    @login_required(login_url='accounts:login')
    def product_create(request):
        try:
            StorAdmin = get_object_or_404(StoreAdminProfile, user=request.user)
            if request.method == 'POST':
                form = ProductForm(request.POST or None, request.FILES or None)
                if form.is_valid():

                    var = Product.objects.create(
                        name=request.POST['name'],
                        price=request.POST['price'],
                        type=request.POST['type'],
                        discount=request.POST['discount'],
                        manufacturer=request.POST['manufacturer'],
                        number_Of_Copy=request.POST['number_Of_Copy'],
                        par_Code=request.POST['par_Code'],
                        product_sections=request.POST['sections'],
                        image=request.FILES['image']
                    )
                    StorAdmin.store.products.add(var)
                    messages.success(request, 'Add product Done.')
                    return redirect('accounts:StoreAdminProfileView')
            else:
                Stor_sections = StorAdmin.store.sections.all()
                sec_list = [sec.name for sec in Stor_sections]
                form = ProductForm()
                form.sec(sec_list=sec_list)
            return render(request, 'product_add_form.html', {'form': form})
        except:
            messages.warning(request,"Make Sure That All Data Is Entered And Correct...!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def update_product(request, pk):
        StorAdmin = get_object_or_404(StoreAdminProfile, user=request.user)
        print(StorAdmin)
        product = get_object_or_404(Product, pk=pk)
        if StorAdmin.store.products.get(pk=pk):
            if request.method == 'POST':
                form = ProductForm(request.POST or None, request.FILES or None, instance=product)
                if form.is_valid():
                    edit = form.save(commit=False)
                    edit.save()
                return redirect('accounts:StoreAdminProfileView')
            else:
                form = ProductForm(instance=product)
                Stor_sections = StorAdmin.store.sections.all()
                print(type(Stor_sections))
                sec_list = [sec.name for sec in Stor_sections]
                form.sec(sec_list=sec_list)
            return render(request, 'product_add_form.html', {'form': form})
        else:
            return Http404

    def delete_product(request, pk):
        StorAdmin = get_object_or_404(StoreAdminProfile, user=request.user)
        product = get_object_or_404(Product, pk=pk)
        if StorAdmin.store.products.get(pk=pk):
            if request.method == 'POST':
                name = product.name
                # StorAdmin.store.products.remove(product)
                obj = get_object_or_404(Product, pk=pk)
                obj.delete()
                messages.success(request, 'Product {0} Delete Done'.format(name))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
