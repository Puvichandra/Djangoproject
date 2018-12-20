from django.shortcuts import render

def index(request):
	return render(request,"home.html",{})
	#my_name="Hello I am Chandrasekar"
	#return render(request,"home.html",{"Puvi":my_name})
	

def about(request):
	return render(request,"about.html",{})
	#from pages.namer import bob
	#return render(request,"about.html",{"my_stuff":bob})
	

def hairoil(request):
	return render(request,"hairoil.html",{})

def Hennadye(request):
	return render(request,"Hennadye.html", {})

def Bathsoap(request):
	return render(request, "Bathsoap.html",{})


# Create your views here.
