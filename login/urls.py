from django.urls import path
from .views import signup,login_view,logout_view
urlpatterns = [
path('',login_view,name="login"),
path('Signup',signup,name='Signup'),
path('logout/', logout_view, name='logout'),



    ]