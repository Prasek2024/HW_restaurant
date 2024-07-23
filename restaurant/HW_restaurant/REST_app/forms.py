from django import forms
from .models import Rest_list


class Restaurant_list(forms.ModelForm):
    class Meta:
        model = Rest_list
        fields = ['restaurant_name', 'type', 'address']