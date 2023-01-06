# Créer un programme qui demandera à l’utilisateur de renseigner un mot et un seul, sans
# espace ni aucun autre caractère que les 26 lettres de l’alphabet (sans accent ni
# majuscule).
# Votre programme devra modifier ce mot, en y changeant de place certains caractères
# (ou tous) afin de donner un mot plus “loin” dans l’ordre alphabétique que le mot
# renseigné par l'utilisateur.
# Attention: Le nouveau mot doit être le mot le plus proche possible, dans l’ordre
# alphabétique, du mot original !
# Par exemple, “abcde” donnerait “abced”. “acedb” est aussi “valide” mais n’est PAS le
# plus proche du mot original dans l’ordre alphabétique.

def rearrange_word(word):
    # Convert the word to a list of characters for easier manipulation
    word_list = [*word]
    # Iterate through the list of characters, starting from the second character
    for i in range(1, len(word_list)):
        # j will be used to iterate backwards through the list of characters
        j = i
        # As long as j is not at the beginning of the list and the character at index j is smaller than the character at index j - 1,
        # swap the characters at indices j and j - 1
        while j > 0 and word_list[j] < word_list[j - 1]:
            word_list[j], word_list[j - 1] = word_list[j - 1], word_list[j]
            j -= 1
        # Return the sorted word as a string
        return ''.join(word_list)


word = input("Entrez un mot : ")
print(rearrange_word(word))

