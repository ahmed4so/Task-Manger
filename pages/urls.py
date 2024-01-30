from django.urls import path
from .views import home,task,account,addtask

urlpatterns = [
    path("",home,name="Home"),
    path("/task",task,name="Tasks"),
    path("/add", addtask, name="add"),
    path("/account", account, name="account"),
]