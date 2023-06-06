NUM = 5
count = 0
while count < NUM:
    count += 1
    if not count % 3:
        continue
    print(count)
else:
    print('Так работает else')

