from django.shortcuts import get_object_or_404, redirect, render
from ManageOffer.forms import OfferForm
from ManageOffer.models import Offer
from ManageStore.models import Store
from accounts.models import StoreAdminProfile
from django.core.paginator import Paginator


def create_offer(request):
    user = get_object_or_404(StoreAdminProfile, user=request.user)
    store = get_object_or_404(Store, id=user.store.pk)
    form = OfferForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        store.StoreOffers.add(form.instance)
        store.save()
        return redirect('accounts:StoreAdminProfileView')
    else:
        form = OfferForm()
    context = {'form': form}

    return render(request, 'create_offer.html', context)


def edit_offer(request, offer_id):
    user = get_object_or_404(StoreAdminProfile, user=request.user)
    store = get_object_or_404(Store, id=user.store.pk)
    offer = get_object_or_404(Offer, id=offer_id)
    if request.method=="POST":
        form = OfferForm(request.POST or None, request.FILES or None, instance=offer)
        if form.is_valid():
            form.save()
            store.StoreOffers.add(form.instance)
            store.save()
            return redirect('accounts:StoreAdminProfileView')
    else:
        form = OfferForm(instance=offer)
    context = {'form': form}
    return render(request, 'Edit_Offer.html', context)


def delete_offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    storeadmin = get_object_or_404(StoreAdminProfile, user=request.user)
    if storeadmin.store.StoreOffers.get(id=offer_id)and request.POST:
        offer.delete()
        return redirect('accounts:StoreAdminProfileView')


def view_offer(request ,offer_id ):
    offer= get_object_or_404(Offer,pk=offer_id )
    return render( request , 'offer_home.html' , {'offer': offer} )


def view_all_offers(request):
    offer=Offer.objects.all()
    paginator = Paginator((offer), 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render( request , 'OfferTemplate.html' , {'offers': offer ,'page_obj': page_obj,} )
