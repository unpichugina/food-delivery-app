from django import forms
from django.contrib.auth import get_user_model
from order.models import Order


class OrderConfirmationForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ('created_at', 'user', 'status', 'total')
        widgets = {'note': forms.Textarea(attrs={'cols': 35, 'rows': 5}),
                   'email': forms.EmailInput,
                   }
