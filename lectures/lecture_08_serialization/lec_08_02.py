# Сериализация
# Преобразоваине Python в JSON

import json

my_dict = {
    'name':'Ivan',
    'age':35,
    'hobbies':['футбол', 'tennis'],
    'children':[
        {
            'name':'Alisa',
            'age':5,
        },
        {
            'name': 'Alisa',
            'age': 5,
        }
    ]
}
print(f'{type(my_dict) = }\n{my_dict = }')
with open('user.json', 'w') as f:
    json.dump(my_dict, f, ensure_ascii=False)

with open('user.json', 'r') as f:
    new_dict = json.load(f)
    print(new_dict)

dict_to_json_text = json.dumps(my_dict)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text}')

res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)
print(res)

