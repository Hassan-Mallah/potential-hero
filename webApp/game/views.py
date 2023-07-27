import random

from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

weapon_options = {
    'Sword': [
        'Engage in a duel with a skilled swordsman to prove your mettle in combat.',
        'Follow a hidden trail that leads to a forgotten swordmaster\'s tomb, seeking to learn ancient sword techniques.',
        'Use your sword to cut through dense vegetation and forge a path deeper into the heart of the forest.'
    ],
    'Bow': [
        'Hunt mystical creatures to gather rare ingredients for a powerful potion.',
        'Join forces with a group of archers to defend the forest from a looming dark threat.',
        'Use your bow to shoot arrows at distant targets, revealing hidden pathways and secrets.'
    ],
    'Axe': [
        'Chop down massive trees to build a bridge across a treacherous chasm.',
        'Confront a group of bandits who have been terrorizing travelers in the forest.',
        'Discover an ancient tree with a hidden axe blade, granting immense strength and vitality to its wielder.'
    ],
    'Staff': [
        'Use your staff to harness the power of the forest and commune with its guardian spirits.',
        'Solve a series of elemental puzzles to unlock the secrets of a mystical portal hidden in the forest.',
        'Channel the energy of the stars to create dazzling displays of light, guiding your way through darkness.'
    ],
    'Dagger': [
        'Sneak through a group of thieves\' camp, using your dagger for silent takedowns.',
        'Uncover a hidden underground cavern where a legendary treasure is said to be guarded by traps.',
        'Use your dagger to collect rare herbs and flowers that grow only in the depths of the forest.'
    ],
    'Gun': [
        'Engage in a thrilling shootout with a gang of outlaws that have infiltrated the forest.',
        'Discover an ancient weapon crafting workshop where you can upgrade your gun with magical ammunition.',
        'Use your gun to fire a special flare into the sky, signaling for help from allies who come to your aid.'
    ]
}

user_session = {}


@csrf_exempt
def index(request: HttpRequest):
    template = loader.get_template('index.html')
    context = {}

    if request.POST:
        step = user_session.get('step', 0)

        if step == 1:
            user_session['step'] = 2

            weapon = request.POST['Radio']

            if weapon:
                context = {
                    'question': 'Nice choice, what\' next?',
                    'answers': weapon_options[weapon]
                }
        else:
            user_session['step'] = 1
            # list of game weapons
            weapons = list(weapon_options.keys())

            context = {
                'question': 'Which weapon would do you like to use?',
                'answers': random.sample(weapons, 3)
            }
    else:
        user_session['step'] = 0
        context['text'] = 'Welcome to Potential Hero, shall we start?'

    return HttpResponse(template.render(context))
