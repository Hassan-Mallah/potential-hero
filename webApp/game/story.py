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


API_KEY = 'API_KEY'
API_URL = 'https://api.rytr.me/v1'


def get_lanugages():
    headers = {'Authentication': f'Bearer {API_KEY}'}
    res = requests.get(f'{API_URL}/languages', headers=headers)

    print(res)
    print(res.json())


# Generate content
def ryte(languageId, toneId, useCaseId, inputContexts):
    try:
        data = {
            'languageId': languageId,
            'toneId': toneId,
            'useCaseId': useCaseId,
            'inputContexts': inputContexts,
            'variations': 1,
            'userId': 'USER1',
            'format': 'html'
        }
        headers = {'Authentication': 'Bearer ' + API_KEY}
        r = requests.post(API_URL + '/ryte', json=data, headers=headers)
        data = r.json()
        return data['data']
    except:
        print('An exception occurred')
    return None


# Use case detail
def useCaseDetail(useCaseId='60ed7113732a5b000cf99e8e'):
    try:
        headers = {'Authentication': 'Bearer ' + API_KEY}
        r = requests.get(API_URL + '/use-cases/' + useCaseId, headers=headers)
        print(r)
        print(r.content)
        data = r.json()
        return data['data']
    except:
        print('An exception occurred')
    return None


def get_test():
    # Step 1 - Identify language ID (use language list API endpoint)
    languageIdEnglish = '607adac76f8fe5000c1e636d'  # English

    # Step 2 - Identify tone ID (use tone list API endpoint)
    toneIdConvincing = '60572a639bdd4272b8fe358b'  # Convincing

    if True:
        # Step 3 - Identify use case ID (use use-case list API endpoint)
        useCaseIdMagicCommand = '60ed7113732a5b000cf99e8e'  # Magic command

        # Step 4 - Identify use case details (use use-case detail API endpoint)
        # useCaseMagicCommand = useCaseDetail(useCaseIdMagicCommand)

        key = 'INPUT_TEXT_LABEL'
        inputContexts = {key: 'Write an email for taking a sick leave'}

        # Step 5 - Generate content (use ryte API endpoint)
        outputs = ryte(
            languageIdEnglish,
            toneIdConvincing,
            useCaseIdMagicCommand,
            inputContexts
        )
        print(outputs)


# get_lanugages()
# useCaseDetail()
get_test()
