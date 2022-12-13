from django.shortcuts import render
from django.template import RequestContext


def handler_not_found(request, exception):
    return render(request, 'main/404.html')


# def handler_server_error(request, exception):
#     return render(request, 'main/500.html', status=500)

def handler_server_error(request):
    context = RequestContext(request)
    response = render('main/500.html', context)
    response.status_code = 500
    return response
