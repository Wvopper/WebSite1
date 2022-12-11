from django.shortcuts import render


def handler_not_found(request, exception):
    return render(request, 'main/404.html')