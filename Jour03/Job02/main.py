def count():
    i = 0
    while i < 20:
       i = i +2
       print(i)


def count_swagger():
    i = 0
    while i < 21:
         if test_pair(i):
            print(i)
            i = i + 1
         else:
            i = i + 1


def test_pair(num):
    if num % 2 == 0:
        return True


count()
count_swagger()