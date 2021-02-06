from django import forms

from ManageStore.models import Store, AD_imags


class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'image',
            'phonesNumber',
            'start_hours',
            'close_hours',
            'description',
            'state',
            'type',
            'url',
        ]


class EditStoreForm(forms.ModelForm):
    new_sections = forms.CharField(label='Add new product_sections', required=False, )

    class Meta:
        model = Store
        fields = [
            'name',
            'image',
            'phonesNumber',
            'start_hours',
            'close_hours',
            'description',
            'state',
            'type',
            'url',
            'new_sections']


class ADForm(forms.ModelForm):
    class Meta():
        model= AD_imags
        fields=['ad_imags']