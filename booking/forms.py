from django import forms
from django.core.exceptions import ValidationError


class RoomsFiltersForm(forms.Form):
    ORDER_BY_CHOICES = (
        ("cost_asc", "Cost Asc"),
        ("cost_desc", "Cost Desc"),
        ("max_price", "Max Cost"),
    )
    cost__gt = forms.IntegerField(min_value=0, label="Cost Min", required=False)
    cost__lt = forms.IntegerField(min_value=0, label="Cost Max", required=False)
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES, required=False)

    def clean(self):
        cleaned_data = super().clean()
        cost__gt = cleaned_data.get("cost__gt")
        cost__lt = cleaned_data.get("cost__lt")
        if cost__gt and cost__lt and cost__gt > cost__lt:
            raise ValidationError("Min price can't be greater than Max price")


class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_come = forms.DateField(help_text="2022-4-3")
    date_out = forms.DateField(help_text="2022-4-3")
    email = forms.EmailField()

