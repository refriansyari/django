from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url('user/',views.user,name='user'),
    url('relative/',views.relative,name='relative'),  
]