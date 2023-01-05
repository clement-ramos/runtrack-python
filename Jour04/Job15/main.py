numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


def string_lenght(string):
    lenght = 0
    for i in string:
        lenght = lenght + 1
    return lenght


def round_number(list):
    for i in range(len(list)):
        if list[i] - int(list[i]) >= 0.5:
            list[i] = int(list[i]) + 1
        else:
            list[i] = int(list[i])

    sort_list(list)
    print(list)
    return list


def sort_list(list):
    print(list)
    list_lenght = string_lenght(list)
    for i in range(list_lenght):
        for j in range(i + 1, (list_lenght)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]


round_number(numbers)