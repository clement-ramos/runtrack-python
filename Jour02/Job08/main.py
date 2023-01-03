def season_vegetable(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("Bonjour vous ne connaissez pas vos saisons")

season_vegetable("legume", "hiver")
season_vegetable("legume", "ete")
season_vegetable("fruits", "hiver")
season_vegetable("fruits", "ete")
season_vegetable("ceci est ", "une erreur")