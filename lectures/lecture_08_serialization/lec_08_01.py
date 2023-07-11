# Сериализация
# Преобразоваине JSON в Python

import json

with open('example.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)

print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["glossary"]["title"]}')

json_text = '''
{
    "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML"
					},
	"GlossTerm": "Standard Generalized Markup Language",
	"Acronym": "SGML"
}
'''
print(f'{type(json_text) = }\n{json_text = }')
json_list = json.loads(json_text)
print(f'{type(json_list) = }\n{len(json_list)}\n{json_list}')

