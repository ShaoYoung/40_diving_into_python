# Сериализация
# Pickle

import pickle

my_dict = {
    'name': 'Ivan',
    'age': 35,
    'hobbies': ['футбол', 'tennis'],
    'children': [
        {
            'name': 'Alisa',
            'age': 5,
        },
        {
            'name': 'Alisa',
            'age': 5,
        }
    ]
}

res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print(f'{res = }')
print(f'{pickle.DEFAULT_PROTOCOL = }')

new_dict = pickle.loads(res)
print(new_dict)

import pickle

my_dict = {'numbers': [42, 4.1415, (7 + 3j)],
           'functions': (sum, max),
           'others': {False, True, 'Hello world!'}
           }
res = pickle.dumps(my_dict)
with open('quest.pickle', 'wb') as f:
    pickle.dump(f'{res = }', f)
