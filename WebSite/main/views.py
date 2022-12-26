from django.shortcuts import render, redirect


def index(request):
    data = {
        'title': 'PHWeb.com. Добро пожаловать'
    }
    return render(request, 'main/main.html', data)


def about(request):
    return render(request, 'main/About.html')


def Kinematika(request):
    data = {
        'title': 'Разделы кинематики'
    }
    return render(request, 'main/Kinematika.html', data)


def dynamik_static(request):
    data = {
        'title': 'Разделы динамики и статики'
    }
    return render(request, 'main/dynamik_statics_page.html', data)


def horizontal_mov(request):
    return render(request, 'main/horizontal_movement.html')