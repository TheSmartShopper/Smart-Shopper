from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from ManageOffer.models import Offer
from ManageProduct.models import Product
from ShoppingCart.models import ShoppingCart, CartItem, CartOffer
from accounts.CustomerProfilemodel import CustomerProfile


def view_shopping_cart(request):
    pass
    user = get_object_or_404(CustomerProfile, user=request.user)
    cart = get_object_or_404(ShoppingCart, id=user.cart.id)

    return render(request, 'view_shopping_cart.html', {
        'cart': cart
    })


def add_product_to_cart(request, product_id, quantity):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    cart = get_object_or_404(ShoppingCart, id=customer.cart.id)
    product = get_object_or_404(Product, id=product_id)
    if product_id in cart.get_product_ids():
        messages.success(request, 'product exists')
    else:
        item = CartItem()
        item.product = product
        item.quantity = quantity
        item.save()
        cart.items.add(item)
        messages.success(request, 'product add Done')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def edit_product_quantity_cart(request, product_id, quantity):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    cart = get_object_or_404(ShoppingCart, id=customer.cart.id)
    if product_id in cart.get_product_ids():
        item = cart.items.get(product_id=product_id)
        if quantity == 0:
            item.delete()
        else:
            item.quantity = quantity
            item.save()
            cart.save()
            messages.success(request, 'product Edit Done')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_offer_to_cart(request, offer_id, quantity):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    cart = get_object_or_404(ShoppingCart, id=customer.cart.id)
    offer = get_object_or_404(Offer, id=offer_id)
    if cart.offers.get(id=offer.id):
        messages.success(request, 'offer exists')
    else:
        new = CartOffer()
        new.Offer = offer
        new.quantity = quantity
        new.save()
        cart.offers.add(new)
        cart.save()
        messages.success(request, 'product add Done')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def edit_offer_quantity_cart(request, CartOffer_id, quantity):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    cart = get_object_or_404(ShoppingCart, id=customer.cart.id)
    offer = cart.items.get(id=CartOffer_id)
    if request.method == 'POST':
        if quantity == 0:
            offer.delete()
        else:
            offer.quantity = quantity
            offer.save()
            cart.save()
            messages.success(request, 'offer Edit Done')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def mainUseCase(request):
    customer = get_object_or_404(CustomerProfile, user=request.user)
    cart = get_object_or_404(ShoppingCart, id=customer.cart.id)

    op1 = []
    op2 = []
    op3 = []

    for P in cart.items.all():
        name = P.product.name
        parCode = P.product.par_Code
        result = Product.objects.filter(name__contains=name)[:2]
        print(result)
        if result.count() >= 3:
            op1.append(result[0])
            op2.append(result[1])
            op3.append(result[2])
        elif result.count() == 2:
            op1.append(result[0])
            op2.append(result[1])
            op3.append(result[1])
        else:
            op1.append(result[0])
            op2.append(result[0])
            op3.append(result[0])

    total1 = sum([p.price for p in op1])
    total2 = sum([p.price for p in op2])
    total3 = sum([p.price for p in op3])

    context = {
        'op1': op1,
        'op2': op2,
        'op3': op3,
        'total1': total1,
        'total2': total2,
        'total3': total3,
    }

    return render(request, 'test.html', context)
