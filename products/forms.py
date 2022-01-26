from django import forms
from .models import Product


# Create your forms here.

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ("category", "name", "image", "description", "price",)

        

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        
        self.fields['category'].widget.attrs['class'] = 'form-control form-select'
        #self.fields['tags'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['description'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['price'].widget.attrs['class'] = 'form-control'

    #def save(self, commit=True):
    #    Product = super(ProductForm, self).save(commit=False)
    #    user.email = self.cleaned_data['email']
    #    if commit:
    #        user.save()
    #    return user
