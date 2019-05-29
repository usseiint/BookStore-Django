from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, Http404


# Create your views here.
def index(request):
	return render(request, 'mainApp/index.html')

def reg(request):
	return render(request, 'mainApp/registration.html')

def signin(request):
	return render(request, 'mainApp/login.html')

def bobo(request):
	return render(request, 'mainApp/books.html')


# def signup(request):
# 	if request.method == 'POST':
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			raw_password = form.cleaned_data.get('password1')
# 			user = authenticate(username=username, password=raw_password)
# 			login(request, user)
# 			return redirect('index')
# 	else:
# 		form = UserCreationForm()
# 	return render(request, 'mainApp/registration.html', {'form': form})
