from __future__ import unicode_literals
from models import Restaurant
from django.shortcuts import render
from django.http import HttpResponse

import json

# Create your views here.
def index(request):
	resp = Restaurant.objects.all()
	return render(request,'index.html',{'resp':resp})

def getlocations(request):
	resp = Restaurant.objects.values_list("name","lat","lon")
	R = []
	for r in resp:
		R.append({"name":r[0],"lat":r[1],"lon":r[2]})
	return HttpResponse(json.dumps(R))