L = [1, 2, 3, 4, 5]

def inverse_first_last(list):
    Temp = list[0]
    list[0] = list[-1]
    list[-1] = Temp
    print(list)


inverse_first_last(L)

