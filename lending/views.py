from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render

def e_handler404(request):
    context = RequestContext(request)
    response = render_to_response('404.html', context)
    response.status_code = 404
    return response

def contact_page(request):
    return render(request, 'contact.html')

def service_page(request):
    return render(request, 'service.html')

def index_page(request):
    return render(request, 'index.html')
