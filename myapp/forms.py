from django import forms
class TestForm(forms.Form):
    name= forms.CharField(max_length=256)
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)