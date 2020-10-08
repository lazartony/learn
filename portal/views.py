from django.shortcuts import render

context = {}


def home(request):
    context['title'] = 'HOME'
    return render(request, 'portal/home.html', context)


def login(request):
    context['title'] = 'LOGIN'
    return render(request, 'portal/login.html', context)
