from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def index(request: HttpRequest):
    print(request.POST)
    context = {
        'question': 'Which weapon would do you like to use?',
        'answers': ['Axe', 'Gun', 'Sword']
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))
