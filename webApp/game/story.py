import random
import requests


def get_random_story():
    when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
    who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
    name = ['Ali', 'Miriam', 'daniel', 'Hoouk', 'Starwalker']
    residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
    went = ['cinema', 'university', 'seminar', 'school', 'laundry']
    happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

    print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(
        residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))


rytr_api = 'API KEY'

url = 'https://api.rytr.me/v1/languages'

headers = {'Authentication': f'Bearer {rytr_api}'}
res = requests.get(url, headers=headers)

print(res)
print(res.json())
