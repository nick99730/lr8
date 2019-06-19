import types
import pickle
from monarchy import Monarchy
from republic import Republic
from kingdom import Kingdom
from state import State


class Error(Exception):
    def __init__(self, *args):
        print(args[0])


class IOStream:
    def __init__(self):
        self._input_data = None
        self._argument = None

    def input_main_arg(self):
        self._input_data = input()
        try:
            int(self._input_data)
        except ValueError:
            raise Error("Invalid choice."
                        " Please enter zero or"
                        " positive integer less than 4.")
        if int(self._input_data) < 0 or int(self._input_data) > 6:
            raise Error("Invalid choice."
                        " Please enter zero or"
                        " positive integer less than 7.")
        return self._input_data

    def input_index(self):
        self._input_data = input()
        try:
            int(self._input_data)
        except ValueError:
            raise Error("Invalid index."
                        " Please enter positive integer.")
        if int(self._input_data) < 0:
            raise Error("Invalid index."
                        " Please enter positive integer.")
        return self._input_data

    def input_data(self):
        data = input()
        self._input_data = data.split()
        self._correct_len()
        self._check_population(self._input_data[0])
        self._check_area(self._input_data[1])
        if int(self._argument) == 1:
            self._check_term(self._input_data[2])
            self._check_number(self._input_data[3])
        elif int(self._argument) == 2 or\
                int(self._argument) == 3:
            self._check_type_of_monarchy(self._input_data[2])
            if int(self._argument) == 3:
                self._check_name_of_monarch(self._input_data[3])
        return self._input_data

    def input_argument(self):
        self._input_data = input()
        try:
            int(self._input_data)
        except ValueError:
            raise Error("Please enter a valid number.")
        if int(self._input_data) != 1 \
                and int(self._input_data) != 2\
                and int(self._input_data) != 3\
                and int(self._input_data) != 4:
            raise Error("Please enter a valid number.")
        self._argument = self._input_data
        return self._input_data

    def input_position(self):
        self._input_data = input()
        try:
            int(self._input_data)
        except ValueError:
            raise Error("Please enter a valid number.")
        if int(self._input_data) != 1 and\
                int(self._input_data) != 2:
            raise Error("Please enter a valid number.")
        return self._input_data

    def _correct_len(self):
        if (int(self._argument) == 1 or
            int(self._argument) == 3)\
                and len(self._input_data) != 4:
            raise Error("Invalid number of values"
                        " ​​entered. Please enter 4 values.")
        elif int(self._argument) == 2 and\
                len(self._input_data) != 3:
            raise Error("Invalid number of values"
                        " ​​entered. Please enter 3 values.")
        elif int(self._argument) == 4 and\
                len(self._input_data) != 2:
            raise Error("Invalid number of "
                        "values ​​entered. Please enter 2 values.")

    @staticmethod
    def _check_area(area):
        try:
            float(area)
        except ValueError:
            raise Error("Please enter a valid area."
                        " Incorrect value: {0}".format(area))
        if float(area) < 0:
            raise Error("Please enter a valid area."
                        " Incorrect value: {0}".format(area))

    @staticmethod
    def _check_population(population):
        try:
            int(population)
        except ValueError:
            raise Error("Please enter a valid population."
                        " Incorrect value:"
                        " {0}".format(population))
        if int(population) < 0:
            raise Error("Please enter a valid population."
                        " Incorrect value:"
                        " {0}".format(population))

    @staticmethod
    def _check_term(term):
        try:
            int(term)
        except ValueError:
            raise Error("Please enter a valid term of government."
                        " Incorrect value: {0}".format(term))
        if int(term) < 0:
            raise Error("Please enter a valid term of government."
                        " Incorrect value: {0}".format(term))

    @staticmethod
    def _check_number(number_of_reelection):
        try:
            int(number_of_reelection)
        except ValueError:
            raise Error("Please enter a"
                        " valid number of reelection."
                        " Incorrect value:"
                        " {0}".format(number_of_reelection))
        if int(number_of_reelection) < 0:
            raise Error("Please enter a valid"
                        "number of reelection."
                        " Incorrect value:"
                        " {0}".format(number_of_reelection))

    @staticmethod
    def _check_type_of_monarchy(type_of_mon):
        if type_of_mon != "absolute" and\
                type_of_mon != "constitutional":
            raise Error("Please enter a valid"
                        " type of monarchy."
                        " Incorrect value:"
                        " {0}".format(type_of_mon))

    @staticmethod
    def _check_name_of_monarch(name_of_mon):
        if not name_of_mon.isalpha():
            raise Error("Please enter a valid"
                        " name of monarch."
                        " Incorrect value: "
                        "{0}".format(name_of_mon))


class List:
    _my_list = []

    @staticmethod
    def _create_republic_instance(words):
        republic = Republic(int(words[0]), float(words[1]),
                            int(words[2]), int(words[3]))
        return republic

    @staticmethod
    def _create_state_instance(words):
        state = State(int(words[0]), float(words[1]))
        return state

    @staticmethod
    def _create_monarchy_instance(words):
        monarchy = Monarchy(int(words[0]), float(words[1]),
                            words[2])
        return monarchy

    @staticmethod
    def _create_kingdom_instance(words):
        kingdom = Kingdom(int(words[0]), float(words[1]),
                          words[2], words[3])
        return kingdom

    def _contains(self, item_type):
        for obj in self._my_list:
            if type(obj).__name__ == item_type:
                return True
        return False

    @staticmethod
    def _get_field_names(cls_name):
        lookup = {'Republic': Republic(), 'Monarchy': Monarchy(),
                  'Kingdom': Kingdom(), 'State': State()}
        my_dict = lookup[cls_name].__dict__
        present_field = []
        is_callable = (types.FunctionType, types.MethodType)
        i = 1
        for key, value in my_dict.items():
            if not isinstance(value, is_callable):
                present_field.append(key)
                ind = key.rindex("__")
                key = key[ind+2:len(key)]
                print("{0} - {1}".format(i, key))
                i += 1
        return present_field

    def _get_object_names(self):
        classes = ["Republic", "Monarchy", "Kingdom", "State"]
        present_cls = []
        index = 0
        for item in classes:
            if self._contains(item):
                print("{0} - {1}".format(index + 1, item))
                present_cls.append(item)
                index += 1
        return present_cls

    def _search(self, class_name, field, sought_value):
        filter_list = list(filter(lambda x:
                                  (type(x).__name__ == class_name
                                   and str(getattr(x, field)) ==
                                   sought_value), self._my_list))
        if len(filter_list) == 0:
            print("Object not found.")
        else:
            print(*list(filter_list), sep='\n\n')

    def print_items(self):
        print(*self._my_list, sep='\n\n')

    def search_switch(self):
        print("Select the object you want to find:")
        present_cls = self._get_object_names()
        obj = int(input())
        print("Select the field you want to search by:")
        present_field = []
        class_name = ""
        if obj == 1:
            present_field = self._get_field_names(present_cls[0])
            class_name = present_cls[0]
        elif obj == 2:
            present_field = self._get_field_names(present_cls[1])
            class_name = present_cls[1]
        elif obj == 3:
            present_field = self._get_field_names(present_cls[2])
            class_name = present_cls[2]
        search_field = int(input())
        print("Enter the value you are looking for:")
        sought_value = input()
        self._search(class_name, present_field[search_field-1], sought_value)

    def _add(self, other):
        return self._my_list.append(other)

    def __getitem__(self, item):
        return self._my_list[item]

    def _ins(self, other, position):
        return self._my_list.insert(position, other)

    def add_item(self, argument, position, words):
        if int(argument) == 1:
            item = self._create_republic_instance(words)
        elif int(argument) == 2:
            item = self._create_monarchy_instance(words)
        elif int(argument) == 3:
            item = self._create_kingdom_instance(words)
        else:
            item = self._create_state_instance(words)
        if position == -1:
            self._add(item)
        else:
            self._ins(item, position)

    def write_file(self):
        with open('text1.pickle', 'ab') as f:
            pickle.dump(self._my_list, f)

    def read_data(self):
        with open('text1.pickle', 'rb') as f:
            instance = pickle.load(f)
        self._my_list += list(instance)

    def _my_sort(self, reverse, class_name=None, field=None):
        if field is None:
            self._my_list.sort(key=lambda x: type(x).__name__, reverse=reverse)
        else:
            max_elem = getattr(max(self._my_list, key=lambda x: getattr(x, field)), field)
            self._my_list.sort(key=lambda x: getattr(x, field)
                               if type(x).__name__ == class_name else max_elem + 1, reverse=reverse)

    def sort_items(self, sort_rep, sort_mon,
                   sort_kingdom, sort_state, revers):
        fields = ["_population", "_area"]
        print("Initial list:")
        print(*self._my_list, sep='\n\n')
        print("\n")
        self._my_sort(revers[0], 'Republic', fields[sort_rep - 1])
        self._my_sort(revers[2], 'Kingdom', fields[sort_kingdom - 1])
        self._my_sort(revers[1], 'Monarchy', fields[sort_mon - 1])
        self._my_sort(revers[3], 'State', fields[sort_state - 1])
        self._my_sort(False)
        print("Sort list:")
        print(*self._my_list, sep='\n\n')
        print("\n")
