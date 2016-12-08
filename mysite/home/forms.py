from django import forms
from parsley.decorators import parsleyfy

@parsleyfy
class SignupForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50)
    email = forms.EmailField()

