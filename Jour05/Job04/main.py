def encoding_like_cesar(string):
        split_string = [*string]
        encoded_alpha = [*"abcdefghijklmnopqrstuvwxyz"]
        i = 0
        for element in split_string:           
            split_string[i] = encoded_alpha[(i+3) % 26] 
            i += 1
        coded_string = "".join(split_string)
        print(coded_string)
 

encoding_like_cesar("Abcde xyz")

# Jules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses
# messages. Sa méthode était assez simple : il décalait les lettres de 3 rangs dans
# l'alphabet.
# Créer une fonction à laquelle on donne un message et un décalage, et la fonction
# renvoie alors le message décalé dans l'alphabet. Il faudra gérer le dépassement ('z'
# décalé vers la droite revient sur 'a', et 'a' décalé vers la gauche revient sur 'z').