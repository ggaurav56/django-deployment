from django import forms
from .models import Order
from django.utils.translation import ugettext_lazy as _

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'address1','address2', 
                  'postal_code', 'city','state',]
        labels = {'phone': _('Mobile Number'),
                  'address1': _('Flat/House and Society'),
                  'address2': _('Locality')}
