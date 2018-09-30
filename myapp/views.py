from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def test_form_view(request):
    form=forms.TestForm()
    if request.method=='POST':
        form= forms.TestForm(request.POST)
        if form.is_valid():
            print('form is valid')
            print('Name:'+form.cleaned_data['name'])
            print('Email:'+form.cleaned_data['email'])
            print('Text:'+form.cleaned_data['text'])
    return render(request,'myapp/testform.html',{'form':form})   
