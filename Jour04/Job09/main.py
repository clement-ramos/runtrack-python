L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def min_max(list):
    max_value = list[0]
    min_value = list[0]
    for element in list:
        if element > max_value:
            max_value = element
            # mise à jour du minimum si nécessaire
        if element < min_value:
            min_value = element

    print(max_value)
    print(min_value)


min_max(L)


