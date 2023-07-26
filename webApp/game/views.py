import random

from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request: HttpRequest):
    template = loader.get_template('index.html')
    context = {}

    if request.POST:
        # list of game weapons
        weapons = ['Sword', 'Bow', 'Axe', 'Staff', 'Dagger', 'Gun']

        context = {
            'question': 'Which weapon would do you like to use?',
            'answers': random.sample(weapons, 3)
        }
    else:
        context['text'] = 'Welcome to Potential Hero, shall we start?'

    return HttpResponse(template.render(context))
