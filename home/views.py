from django.shortcuts import render


def login(request):
    return render(request, 'home/home.html')


def main(request):
    return render(request, 'home/main.html')
