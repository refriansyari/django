from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url('registration/',views.registration,name='registration'),
    url('user_login/',views.user_login,name='user_login'), 
]