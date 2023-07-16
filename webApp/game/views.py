from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def index(request: HttpRequest):
    print(request.POST)

    template = loader.get_template('index.html')
    return HttpResponse(template.render({}))
