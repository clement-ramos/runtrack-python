L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def sum_pair(list):
    total = 0
    for element in list:
        if (element % 2) == 0:
            total = total + element

    print(total)

    
sum_pair(L)

