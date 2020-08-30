from django.shortcuts import render
from django.http import HttpResponse
from . import scripts

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're entering the virtual reef viewer!")

# scripts
def syncUpc(request):
	dataSycned = scripts.fetchUpcData()
	#for row in df.rows:
	#	get_or_create

	return HttpResponse("We synced the UPC data: " + str(dataSycned))


