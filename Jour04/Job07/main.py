L = [8, 24,48,2,16]

def count_divide_by3(list):
    divider = 0
    for element in list:
        if element % 3 == 0:
            divider += 1
    print(divider)


count_divide_by3(L)

