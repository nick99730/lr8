from abc import ABC, abstractmethod
from functools import reduce


class Interface(ABC):
    @abstractmethod
    def my_method(self, list_items: list) -> float:
        pass


class MyClass(Interface):
    def __new__(cls, arg):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MyClass, cls).__new__(cls, arg)
        return cls.instance

    def __init__(self, arg=None):
        self.__arg = arg

    def my_method(self, my_list):
        if self.__arg == 1:
            return reduce((lambda a, b: a if a < b else b), my_list)
        elif self.__arg == 2:
            return reduce((lambda a, b: a + b), my_list)


main_list = list()
while True:
    print("1 - finding the minimum element of an array.")
    print("2 - sum of all array elements.")
    print("3 - add item.")
    print("0 - exit.")
    main_arg = int(input())
    if main_arg == 0:
        break
    elif main_arg == 3:
        print("Enter the item you want to add: ")
        item = float(input())
        main_list.append(item)
        continue
    obj = MyClass(main_arg)
    print(obj.my_method(main_list))
