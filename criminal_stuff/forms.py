from django import forms
from .models import Criminal
class SearchForm(forms.Form):
    upload_image = forms.FileField()

# class RegisterCriminalForm(forms.ModelForm):
#     class Meta:
#         model = Criminal
#         fields = '__all__'