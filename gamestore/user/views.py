from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from astroid import objects
from django.contrib.auth import authenticate, login, logout
from gamehome.models import User
# Create your views here.
def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('register')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    return render(request, template_name='user/login.html', context=context)


def register(request):
    if request.method == 'POST':
        r = User()
        r.username = request.POST.get('username')
        r.password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        r.first_name = request.POST.get('first_name')
        r.last_name = request.POST.get('last_name')
        r.email = request.POST.get('email')
        if r.password == c_password:
            r.save()
            return redirect('login')
        # else:
            
        #     error = 'Wrong username or password!'
        
    return render(request, 'user/register.html')