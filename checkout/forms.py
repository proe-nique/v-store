from django import forms
from .models import BillingAddress


# Create your forms here.

class BillingAddressForm(forms.ModelForm):
    
    class Meta:
        model = BillingAddress
        fields = ("address", "zipcode", "city", "landmark",)

        

    def __init__(self, *args, **kwargs):
        super(BillingAddressForm, self).__init__(*args, **kwargs)
        
        self.fields['address'].widget.attrs['class'] = 'form-control form-select'
        #self.fields['tags'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['zipcode'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['landmark'].widget.attrs['class'] = 'form-control mb-2'
        #self.fields['price'].widget.attrs['class'] = 'form-control'