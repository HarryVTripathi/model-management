from django.shortcuts import render
from django.http import HttpResponse

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
  return HttpResponse(response['data'])

def about(request):
  text = ''
  with open('../README.md') as file:
    text = file.read()

  return HttpResponse(text)

