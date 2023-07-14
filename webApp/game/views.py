from django.http import HttpResponse, HttpRequest
from django.template import loader


# Create your views here.

def index(request: HttpRequest):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}))
