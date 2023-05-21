from django import forms
from django.forms import ModelForm
from shop.models import Product


class CartAddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['sizes']

    def __init__(self, pk, *args, **kwargs):
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        sizes = tuple(Product.objects.get(pk=pk).sizes)
        sizes_list = []
        for item in sizes:
            sizes_list.append((item, item))
        self.fields['sizes'] = forms.ChoiceField(choices=sizes_list)