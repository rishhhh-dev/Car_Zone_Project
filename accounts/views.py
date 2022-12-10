from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
# Create your views here.


def Register(request):
	if request.method == 'POST':

		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		if password == confirm_password:
			if User.objects.filter(username = username).exists():
				messages.error(request,'Username already exists')
				return redirect('register')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request,'Email already exists')
					return redirect('register')	
				else:
					user = User.objects.create_user(first_name=firstname,last_name=lastname,
						username=username,password=password)
					user.save()
					messages.success(request,'You are registered successfully!')
					return redirect('login')
		else:
			messages.error(request,'Password does not match')
			return redirect('register')

		# return redirect('register')
		
	else:
		return render(request,'accounts/sign_up.html')


def Login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			messages.success(request,'You are logged in successfuly')
			return redirect('dashboard')

		else:
			messages.error(request,"Invalid login credentials")
			return redirect('login')
	else:
		return render(request,'accounts/login.html')


@login_required(login_url='login')
def Dashboard(request):
	user_enquiry = Contact.objects.order_by('-created_date')
	data = {
		'enquires' : user_enquiry,
	}
	return render(request,'accounts/dashboard.html',data)


def Logout(request):
	if request.method == 'POST':
		auth.logout(request)
		
	
	return redirect('home')

