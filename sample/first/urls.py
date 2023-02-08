from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index") ,
    path("abc", views.third, name="abc" ) ,
    path("new", views.new, name="new" )
]