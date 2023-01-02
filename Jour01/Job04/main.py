def print_straight():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    array = list(alphabet)
    for letter in array:
        print(letter)

def print_reverse():
    alphabet = "abcdefghijklmnopqrstuvwxyz" [::-1]
    array = list(alphabet)
    for letter in array:
        print(letter)

def print_alphabet(choice):
    if choice == 0:
        print_straight()
    elif choice == 1:
        print_reverse()
    else:
        print("Only 0 and 1 are avaiable parameter")

print_alphabet(0)
print_alphabet(1)