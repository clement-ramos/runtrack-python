def sign(number):
    if type(number) is int or type(number) is float:

        if number == 0:
            print("Ce chiffre est 0 !")
        elif number < 0:
            print("Negatif Chef !")
        elif number > 0:
            print("Positif !")
    else:
        print("Le parametre choisi n'est pas un chiffre")

sign(-4)
sign(2)
sign(0)
sign("abf")