def split_string(no_split_string):
    split_string = []
    delimiter = " "
    start = 0
    end = 0
    n = string_lenght(no_split_string)
    while end < n:
        if no_split_string[end] == delimiter:
            split_string += [(no_split_string[start:end])]
            start = end + 1
        end += 1
    split_string += [(no_split_string[start:])]
    print(split_string)
    return split_string


def string_lenght(string):
    lenght = 0
    for i in string:
        lenght = lenght + 1
    return lenght


def my_long_word(num, my_text):
    my_final_string = []
    for element in split_string(my_text):
        word_lenght = string_lenght(element)
        if word_lenght > num:
            my_final_string += [element]

    print(my_final_string)
    return my_final_string

my_long_word(2,"La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance")