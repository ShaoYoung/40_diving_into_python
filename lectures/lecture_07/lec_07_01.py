# Файлы и файловая система

f = open('text_data.txt', encoding='utf-8')
print(f)
print(list(f))
f.close()

f = open('text_data.txt', 'a', encoding='utf-8')
f.write('Окончание файла\n')
f.close()

f = open('bin_data', 'wb', buffering=64)
f.write(b'X' * 1200)
f.close()
