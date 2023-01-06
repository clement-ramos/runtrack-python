def encoding_like_cesar(string):
        split_string = ""
        alpha = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        while i < len(string):
            j = 0
            while j < len(alpha):
                if string[i].lower() == alpha[j]:
                    split_string += alpha[(j + 3) % len(alpha)]
                j += 1

            i += 1
        return split_string


msg = "Bonjour"
print(encoding_like_cesar(msg))


# Jules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses
# messages. Sa méthode était assez simple : il décalait les lettres de 3 rangs dans
# l'alphabet.
# Créer une fonction à laquelle on donne un message et un décalage, et la fonction
# renvoie alors le message décalé dans l'alphabet. Il faudra gérer le dépassement ('z'
# décalé vers la droite revient sur 'a', et 'a' décalé vers la gauche revient sur 'z').