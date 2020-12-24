from django.conf.urls import url
from first_app import views


urlpatterns = [
    url('',views.index,name='index'),
    url('',views.form_name_view,name='form_page'),  
]