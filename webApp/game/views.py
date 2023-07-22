from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request: HttpRequest):
    template = loader.get_template('index.html')
    context = {}

    if request.POST:
        context = {
            'question': 'Which weapon would do you like to use?',
            'answers': ['Axe', 'Gun', 'Sword']
        }
    else:
        context['text'] = 'Welcome to Potential Hero, shall we start?'

    return HttpResponse(template.render(context))
