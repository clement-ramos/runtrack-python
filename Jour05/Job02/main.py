def draw_rectangle(width, height):

    side = "|"
    top = "-"
    for i in range(height):
        if i == 0 or i == height - 1:
            print(side + (top * (width - 2)) + side)
        else:
            print(side + (' ' * (width - 2)) + side)


# Écrire un programme qui affiche dans le terminal un rectangle avec des ‘-’ et des ‘|’ en
# fonction des paramètres d’entrées, (width, height), par exemple :

draw_rectangle(10, 5)