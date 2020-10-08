from django.shortcuts import render

context = {}


def home(request):
    context['title'] = 'HOME'
    return render(request, 'portal/home.html', context)
