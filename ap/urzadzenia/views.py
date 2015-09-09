from django.http import HttpRequest

from django.shortcuts import render






def profile(request):
    return render(request, 'urzadzenia/base.html')

