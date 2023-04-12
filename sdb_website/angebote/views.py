from django.shortcuts import render

def home(request):
	return render(request, 'angebote/home.html', {})