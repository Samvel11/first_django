from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("Hello DJango world!")

def name(request):
	return HttpResponse("I'm Samvel Simonyan")
