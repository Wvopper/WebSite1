from django.shortcuts import render, redirect


def index(request):
    data = {
        'title': 'The main page of the site'    
            }
    return render(request, 'main/temp_2_copy.html', data)


def Knematika(request):
    data = {
        'title': 'Разделы кинематики'
            }
    return render(request, 'main/Kinematika.html', data)


# def main(request):
#     data = {
#         'title': 'Tets page'
#     }
#     return render(request, 'main/temp_2_copy.html')