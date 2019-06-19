from class_list import List, IOStream, Error
a = List()
stream = IOStream()


def data_input(argument, position):
    while True:
        print("Enter element data through the space:\n")
        try:
            words = stream.input_data()
        except Error:
            continue
        break
    a.add_item(argument, position, words)


def add_switch():
    while True:
        print("1 - add Republic instance.")
        print("2 - add Monarchy instance.")
        print("3 - add Kingdom instance.")
        print("4 - add State instance.")
        try:
            argument = stream.input_argument()
        except Error:
            continue
        break
    while True:
        print("1 - add to the end of the list.")
        print("2 - add to a certain place in the list.")
        try:
            position = int(stream.input_position())
        except Error:
            continue
        break
    if position == 2:
        while True:
            print("Enter index:\n")
            try:
                position = int(stream.input_index())
            except Error:
                continue
            break
    else:
        position = -1
    data_input(argument, position)


def sort_menu(class_name):
    input_list = []
    print("Select sorting type for {0}:".format(class_name))
    print("0 - forward.")
    print("1 - reverse.")
    input_list.append(bool(int(input())))
    print("Select the field by which you want"
          " to sort objects of type {0}:".format(class_name))
    print("1 - population.")
    print("2 - area.")
    input_list.append(int(input()))
    return input_list


def sort_switch():
    revers = [False, False, False, False]
    input_list = sort_menu('Republic')
    revers[0] = input_list[0]
    sort_republic = input_list[1]
    input_list = sort_menu('Monarchy')
    revers[1] = input_list[0]
    sort_monarchy = input_list[1]
    input_list = sort_menu('Kingdom')
    revers[2] = input_list[0]
    sort_kingdom = input_list[1]
    input_list = sort_menu('State')
    revers[3] = input_list[0]
    sort_state = input_list[1]
    return a.sort_items(sort_republic,
                        sort_monarchy, sort_kingdom,
                        sort_state, revers)


def main_switch(argument):
    if argument == 1:
        return add_switch()
    elif argument == 2:
        return sort_switch()
    elif argument == 3:
        return a.search_switch()
    elif argument == 4:
        return a.write_file()
    elif argument == 5:
        return a.read_data()
    elif argument == 6:
        a.print_items()


while 1:
    print("1 - add.")
    print("2 - sort list.")
    print("3 - list search.")
    print("4 - write to file")
    print("5 - read file")
    print("6 - print list")
    print("0 - exit.")
    try:
        x = int(stream.input_main_arg())
    except Error:
        continue
    else:
        if x is 0:
            break
        main_switch(x)
