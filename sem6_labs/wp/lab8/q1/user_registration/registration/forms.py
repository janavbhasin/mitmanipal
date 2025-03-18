from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, label='UserName', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=False)
    email = forms.EmailField(label='Email ID', required=False)
    contact = forms.CharField(max_length=15, label='Contact Number', required=False)
