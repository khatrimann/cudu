from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html', {})


def shop1(request):
    return render(request, 'app/electronics.html', {})
