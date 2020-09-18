from django.shortcuts import render
from django.http import HttpResponse
from . import scripts

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're entering the virtual reef viewer!")

# scripts
def syncUpc(request):
	dataSynced = scripts.fetchUpcData()
	return HttpResponse("We synced the UPC data: " + str(dataSynced))

def syncInvert(request):
	dataSynced = scripts.fetchInvertebrateData()
	return HttpResponse("We synced the Invert data: " + str(dataSynced))
	