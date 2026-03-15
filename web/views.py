from django.shortcuts import render


def app_home(request):
	return render(request, 'web/app_home.html')

# Create your views here.
