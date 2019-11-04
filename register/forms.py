from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=True)

    first_name.label = 'Full Name'
    email.label = 'University Email'

    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'email',
            'password1',
            'password2'
            ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        # self.fields['password1'].help_text = 'Password must contain minimum 1 letter, 1 number & 6 digits.'
        self.fields['username'].help_text = 'Ex. 123-45-6789'
        self.fields['username'].label = 'Username(University ID)'
        self.fields['password2'].help_text = None
        # for fldname in ['username', 'password1', 'password2']:
        #     self.fields[fldname].help_text = None

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if email != 'wahiatasnim@gmail.com':
            if not email.endswith('@diu.edu.bd'):
                raise forms.ValidationError("Enter university email.", code='Not a g-suite mail')
            elif User.objects.filter(email=email):
                raise forms.ValidationError("Email already used. If you forget your password, reset it.", code="Used email.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == 'tasnimridi':
            return username
        cnt = username.count('-')
        numeric = username.replace('-', '')
        if cnt != 2 or not numeric.isnumeric():
            raise forms.ValidationError("Enter ID with correct format.")
        return username

    def __str__(self):
        return self.username


class LoginForm(AuthenticationForm):
    class Meta:
        Model = AuthenticationForm
        fields = [
            'username',
            'password',
        ]

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'University ID'
        self.fields['username'].widget.attrs['placeholder'] = '123-45-7890'
        self.fields['password'].label = 'Password'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

