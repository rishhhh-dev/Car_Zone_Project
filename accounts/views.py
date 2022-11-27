from django.shortcuts import render,redirect

# Create your views here.


def Register(request):
	return render(request,'accounts/register.html')


def Login(request):
	return render(request,'accounts/login.html')


def Dashboard(request):
	return render(request,'accounts/dashboard.html')


def Logout(request):
	return redirect('home')