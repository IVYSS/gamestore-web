from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from astroid import objects
from django.contrib.auth import authenticate, login, logout
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


def register(requsrt):
    return HttpResponse("register")