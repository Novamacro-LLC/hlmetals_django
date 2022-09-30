from django.shortcuts import render


def main(request):
    return render(request, 'home/../account/templates/main.html')
