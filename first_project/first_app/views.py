from django.shortcuts import render
# from django.http import HttpResponse
from first_app.forms import UserForm,UserProfileInfoForm
# from first_app.models import User
# from first_app.forms import NewUserForm
from first_app import views

def index(request):
    return render(request,'first_app/index.html')

def user(request):
    return render(request,'first_app/user.html')

def relative(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES['profile_pics']
                profile.save()
                
                registered = True
        else:
            print(user_form.errors,profile_form.errors)
        
    else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()

    return render(request,'first_app/relative_url_templates.html',
                                {'user_form':user_form,
                                'profile_form':profile_form,
                                'registered':registered})


    


# def user(request):

#     form = NewUserForm()

#     if request.method =="POST":
#         form = NewUserForm(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
        
#         else:
#             print('ERROR FORM INVALID')

#     return render(request,'first_app/user.html',{'form':form})
# from first_app.models import Topic,Webpage,AccessRecord
# from . import forms
# from .forms import FormName
# Create your views here.

# def index(request):
#     webpages_list = AccessRecord.objects.order_by('date')
#     date_dictionary = {'access_records':webpages_list}
#     return render(request,'first_app/index.html',context=date_dictionary)


# def form_name_view(request):
#     form = forms.FormName()


#     if request.method == 'POST':
#         form = forms.FormName(request.POST)

#         if form.is_valid():
#             print("VALIDATION SUCCESS!")
#         print("NAME: "+form.cleaned_data['name'])
#         print("EMAIL: "+form.cleaned_data['email'])
#         print("TEXT: "+form.cleaned_data['text'])

# def index(request):
#     return render(request,'first_app/index.html', context_dict)





#     return render(request,'first_app/form_page.html',{'forms':form})