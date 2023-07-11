data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for item in data:
    print(item)

for _ in data:
    print('item')

NUM = 10
for i in range(0, NUM, 2):
    print(i, end=' ')
print()

animals = ['cat', 'dog', 'wolf']
for i, animal in enumerate(animals, start=100):
    print(i, animal)
