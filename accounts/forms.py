from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))