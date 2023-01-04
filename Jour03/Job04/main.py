def count():
    i = 0
    while i < 101:
        if there_are_no_rest(i, 5) and there_are_no_rest(i, 3):
            print("FizzBuzz")
            i = i + 1
        elif there_are_no_rest(i, 3):
            print("Fizz")
            i = i + 1
        elif there_are_no_rest(i, 5):
            print("Buzz")
            i = i + 1
        else:
            i = i + 1


def there_are_no_rest(num, div):
    if num % div == 0:
        return True


count()

