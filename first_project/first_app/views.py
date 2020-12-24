from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from . import forms
from .forms import FormName
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dictionary = {'access_records':webpages_list}
    return render(request,'first_app/index.html',context=date_dictionary)

def form_name_view(request):
    form = forms.FormName()


    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():

            print("VALIDATION SUCCESS!")
        #GRAB DATA
        print("NAME: "+form.cleaned_data['name'])
        print("EMAIL: "+form.cleaned_data['email'])
        print("TEXT: "+form.cleaned_data['text'])





    return render(request,'first_app/form_page.html',{'forms':form})