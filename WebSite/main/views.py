from django.shortcuts import render, redirect



def index(request):
    data = {
        'title': 'The main page of the site'
            }
    return render(request, 'main/main.html', data)


def about(request):
    return render(request, 'main/About.html')


# def not_found(request, exception):
#     return render(request, 'main/404.html')


def Kinematika(request):
    data = {
        'title': 'Разделы кинематики'
            }
    return render(request, 'main/Kinematika.html', data)