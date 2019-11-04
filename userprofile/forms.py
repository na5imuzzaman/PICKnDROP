from django import forms
from .models import ProfileEdit


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileEdit
        fields = [
            'displayPicture',
            'hallName',
            'roomNumber',
            'contact1',
            'contact2',
        ]