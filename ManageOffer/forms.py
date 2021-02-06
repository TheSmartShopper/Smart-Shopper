from ManageOffer.models import Offer
from django import forms


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'
        exclude = ['StoreId','slug']