from django.http import HttpResponse
from django.shortcuts import render

tasks=["Navateja","Manohar","Jyothi","Vinoothna"]

# Create your views here.
def index(request):
    return HttpResponse("ABC")

def third(request):
    return render(request, "first/index.html")

def new(request):
    return render(request, "first/newtasks.html" ,{
        "tasks":tasks
    })