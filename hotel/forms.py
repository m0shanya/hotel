from django import forms
from django.core.validators import RegexValidator


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    valid = RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}$',
                           'only double case characters, special characters and numbers')
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=6, widget=forms.PasswordInput(), validators=[valid]
    )
    password_repeat = forms.CharField(
        min_length=6, widget=forms.PasswordInput(), validators=[valid]
    )

    def clean_password_repeat(self):
        if self.cleaned_data['password'] != self.cleaned_data['password_repeat']:
            raise forms.ValidationError('Passwords don\'t match.')
        return self.cleaned_data['password_repeat']

    def password_validation(self):
        if self.cleaned_data['password'] not in self.valid:
            raise forms.ValidationError('Password is invalid')
        return self.cleaned_data['password']
