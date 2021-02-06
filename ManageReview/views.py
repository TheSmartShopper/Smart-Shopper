from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from ManageOffer.models import Offer
from ManageProduct.models import Product
from ManageReview.forms import ReviewForm
from ManageReview.models import Review
from ManageStore.models import Store
from accounts.CustomerProfilemodel import CustomerProfile


def add_product_review(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        user = get_object_or_404(CustomerProfile, user=request.user)
        if request.POST['text'] != '':

            review = Review.objects.create(
                text=request.POST['text'],
                rating=request.POST['rating']
            )
            review.save()
            user.review.add(review)
            product.ProductReview.add(review)
        else:
            messages.warning(request, 'Enter valid Review . . .')
    except Exception:
        messages.warning(request, "you can\'t post Review ...")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_store_review(request, store_id):
    try:
        store = get_object_or_404(Store, id=store_id)
        user = get_object_or_404(CustomerProfile, user=request.user)

        if request.POST['text'] != '':

            review = Review.objects.create(

                text=request.POST['text'],
                rating=request.POST['rating']
            )
            review.save()
            user.review.add(review)
            store.StoreReviews.add(review)
        else:
            messages.warning(request, 'Enter valid Review . . .')
    except Exception:
        messages.warning(request, "you can't post Review ...")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_offer_review(request, offer_id):
    try:
        user = get_object_or_404(CustomerProfile, user=request.user)
        offer = get_object_or_404(Offer, id=offer_id)

        if request.POST['text'] != '':

            review = Review.objects.create(
                text=request.POST['text'],
                rating=request.POST['rating']
            )
            review.save()
            user.review.add(review)
            offer.review.add(review)
        else:
            messages.warning(request, 'Enter valid Review . . .')
    except Exception:
        messages.warning(request, "you can\'t post Review ...")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def s(request):
    review = Review.objects.get(id=1)
    user = get_object_or_404(CustomerProfile, id=review.author)
    return render(request, 'review_card.html', {"review": review})


def edit_review(request, review_id):
    user = get_object_or_404(CustomerProfile, user=request.user)
    review = get_object_or_404(Review, id=review_id)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        review.save()
    else:
        form = ReviewForm(instance=review)
    context = {'form': form}
    return render(request, 'x.html', context)
