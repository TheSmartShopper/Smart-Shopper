from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    # sections = forms.CharField(max_length=20)

    class Meta:
        model = Product
        fields = ['name',
                  'price',
                  'image',
                  'type',
                  'discount',
                  'manufacturer',
                  'number_Of_Copy',
                  'par_Code',
                  ]
    def sec(self, sec_list):
        self.sections = forms.CharField(widget=forms.Select(choices=[(sec, sec) for sec in sec_list]),max_length=20)
        self.fields['sections'] = self.sections
