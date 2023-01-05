L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def count_lenght(list):
    lenght = 0
    for element in list:
        lenght += 1
    return lenght

def sort_list(list):
    print(list)
    list_lenght = count_lenght(list)
    for i in range(list_lenght):
        for j in range(i + 1, (list_lenght)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    print(list)


sort_list(L)
