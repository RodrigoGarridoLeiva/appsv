from django.shortcuts import render

def primero(request):

	return render(request,"primero.html")

def segundo(request):

	return render(request,"segundo.html")

def tercero(request):

	return render(request,"tercero.html")

def cuarto(request):

	return render(request,"cuarto.html")

def quinto(request):

	return render(request,"quinto.html")

def escapa(request):

	return render(request,"escapa.html")

def final(request):

	return render(request,"final.html")