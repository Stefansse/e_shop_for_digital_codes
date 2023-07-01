# forms.py

from django import forms
from .models import Payment, Order

from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['order', 'payment_date', 'payment_method']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['order'].queryset = Order.objects.filter(user=self.user)
            self.instance.user = self.user
