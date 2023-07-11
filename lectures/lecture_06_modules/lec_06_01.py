# Модули

# import sys
# print(sys)
# print(sys.builtin_module_names)
# print(*sys.path, sep='\n')


# from sys import builtin_module_names, path
# print(builtin_module_names)
# print(*path, sep='\n')

def empty():
    return 'qwerty'

from sys import builtin_module_names as bmn, path as p

if __name__ == '__main__':
    print(bmn)
    print(*p, sep='\n')

