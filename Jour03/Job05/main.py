def count():
    i = 1
    while i < 1001:
        if is_premier(i):
            print(i)
            i = i + 1
        else:
            i = i + 1


def is_premier(num):
    divider = 0
    i = 1
    while i < num:
        if num % i == 0:
            divider = divider + 1
            i = i + 1
        else:
            i = i + 1

    if divider == 1:
        return True
    else:
        return False


count()

