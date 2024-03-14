from django.shortcuts import render , redirect
from django.http import HttpResponse
from django import forms
# Create your views here.
 
class NewForm(forms.Form):
    name = forms.CharField(label="Name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

   

class person:
    def __init__(self,name,password):
        self.name = name
        self.password = password

people = []
       

def index(request):
    return render(request,"app/names.html",{"people": people})

def add(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            new_person = person(name,password)
            people.append(new_person) 
            return redirect('index')
            
    else:
        form = NewForm()
    return render(request,"app/add.html",{"form": form})