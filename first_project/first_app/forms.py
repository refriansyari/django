from django import forms

class  FormName(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)