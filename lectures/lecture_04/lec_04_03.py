# функции
# *args, **kwargs

def mean(*args):
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))
print(mean(1))
# print(mean([1,2,3]))      # ошибка


def school(**kwargs):
    for key,value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')

school(химия=5, физика=4, qwerty=3, zxc=2, qaz_1=1)




