from django import forms
from flatpickr import DatePickerInput
from .models import PostOrderRequest


class PostOrderRequestForm(forms.ModelForm):
    weight = forms.DecimalField(max_value=5.0, label='Weight(KG)',
                                widget=forms.TextInput(attrs={'placeholder': 'max: 5'}))
    # date = forms.DateField(widget=Date)

    class Meta:
        model = PostOrderRequest
        fields = [
            # 'author',
            'pickupPointType',
            'pickupPoint',
            'pickupPointDescription',
            'deliveryPoint',
            'parcelType',
            'parcelDescription',
            'weight',
            'deliveryDate',
        ]
        widgets = {
            'deliveryDate': DatePickerInput().start_of('event days'),
        }