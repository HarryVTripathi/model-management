from django.shortcuts import render
from django.http import HttpResponse
from fashionmodels.models import FashionModel

# Create your views here. This is where
# we have to write the actual code for
# our webpage.

# Make sure that the code we write here
# is seen and run by Django


# The method below takes in request and
# returns http response. Handles http
# request for the view page of the site.

def welcome(request):
  print(request.method)
  # print(request.META)
  # print(request.headers)
  # print(request.urlconf)
  response = {
    "data": "Welcome to Zigler Model Portfolio Management"
  }

  # Every time django receives a request for this page,
  # view-function will pass this dictionary to the template
  # variable. Dynamic template.
  return render(request, "website/welcome.html", 
  {
    "mesqsage": "This data was sent from the template",
    "fashion_models": FashionModel.objects.all()
  }) 

def about(request):
  text = ''
  with open('../README.md') as file:
    text = file.read()

  return HttpResponse(text)

