L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def in_inter(list):
    num_in_range = 0
    max = 90
    min = 25
    for element in list:
        if (element > min and element < max):
            num_in_range += 1

    print(num_in_range)

in_inter(L)



