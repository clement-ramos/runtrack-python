# Écrire une fonction qui, recevant une taille n en paramètre, affiche un tapis de n+1
# lignes/n+1 colonnes traversé par une diagonale.
# Exemple pour une taille de 10 :

def draw_tapis(n):

    side = "|"
    top = "-"
    corner = "+"
    carpet = "#"
    real_size = n + 1
    blank_pos = n 
    for i in range(real_size):
        if i == 0 or i == real_size - 1:
            print(corner + (top * (real_size - 2)) + corner)

        else:  
            print(side + (carpet * (blank_pos - 2))+ " " + (carpet * (n - blank_pos))+ side)
            blank_pos = blank_pos - 1
           


draw_tapis(5)