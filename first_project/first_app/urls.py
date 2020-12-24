from django.conf.urls import url
from first_app import views


urlpatterns = [
    url('',views.user,name='user'),  
]