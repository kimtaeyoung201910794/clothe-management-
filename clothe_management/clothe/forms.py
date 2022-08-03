from django import forms
from .models import clothe

class clotheForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    category = forms.CharField(max_length=20)
    season = forms.CharField(max_length=20)
    style = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    memo = forms.CharField(max_length=20)



    class Meta:
        model = clothe
        fields = ("name", "category", "season", "style", "color","memo")