# Задание
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from hw_10_classes import Fish, Bird, Human


# вариант через возврат экземпляра созданного класса
class FirstFabric:
    # @staticmethod – используется для создания метода, который ничего не знает о классе или экземпляре, через который он был вызван.
    # Он просто получает переданные аргументы, без неявного первого аргумента, и его определение неизменяемо через наследование.
    # Проще говоря, @staticmethod – это вроде обычной функции, определенной внутри класса, которая не имеет доступа к экземпляру,
    # поэтому ее можно вызывать без создания экземпляра класса.
    @staticmethod
    def get_animal(animal_type, *args):
        dict_classes = {'fish': Fish,
                        'bird': Bird,
                        'human': Human
                        }
        # если тип указан строкой
        if isinstance(animal_type, str):
            return dict_classes[animal_type](*args)
        # если тип указан явно
        elif animal_type in dict_classes.values():
            return animal_type(*args)
        # иначе возврат None


# вариант через создание атрибута animal класса Fabric
class SecondFabric:
    dict_classes = {'fish': Fish,
                    'bird': Bird,
                    'human': Human
                    }

    def __init__(self, animal_type, *args):
        if isinstance(animal_type, str):
            self.animal = self.dict_classes[animal_type](*args)
        elif animal_type in self.dict_classes.values():
            self.animal = animal_type(*args)


if __name__ == '__main__':
    item = FirstFabric.get_animal('fish', 'Карась', 1)
    print(f'{item.name = :<20} {type(item) = }\t{item.get_specific() = }')
    item = FirstFabric.get_animal(Bird, 'Орёл', 1)
    print(f'{item.name = :<20} {type(item) = }\t{item.get_specific() = }')
    item = FirstFabric.get_animal('human', 'Василий Алибабаевич', 1)
    print(f'{item.name = :<20} {type(item) = }\t{item.get_specific() = }')

    item = SecondFabric('fish', 'Карась', 1)
    print(f'{item.animal.name = :<20} {type(item.animal) = }\t{item.animal.get_specific() = }')
    item = SecondFabric(Bird, 'Орёл', 1)
    print(f'{item.animal.name = :<20} {type(item.animal) = }\t{item.animal.get_specific() = }')
    item = SecondFabric('human', 'Василий Алибабаевич', 1)
    print(f'{item.animal.name = :<20} {type(item.animal) = }\t{item.animal.get_specific() = }')
