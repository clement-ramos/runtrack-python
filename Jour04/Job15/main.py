numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# This function takes a string as input and returns the length of the string
def string_lenght(string):
    lenght = 0
    for i in string:
        lenght = lenght + 1
    return lenght


# This function sorts the list in ascending order
def sort_list(list):
    print(list)
    # This gets the length of the list
    list_lenght = string_lenght(list)
    # This nested loop goes through the list and compares each element to the rest of the elements
    # If an element is greater than another element, it swaps the two elements
    for i in range(list_lenght):
        for j in range(i + 1, (list_lenght)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

# This function takes a list of numbers as input and rounds each number

# If the number is equal or above 0.5, it rounds up to the nearest integer
# Otherwise, it rounds down to the nearest integer

# It then sorts the list in ascending order and prints the list
def round_number(list):
    for i in range(len(list)):
        if list[i] - int(list[i]) >= 0.5:
            list[i] = int(list[i]) + 1
        else:
            list[i] = int(list[i])

    # calling the sorting function
    sort_list(list)
    print(list)
    return list


round_number(numbers)