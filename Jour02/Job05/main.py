def calcul(num1, operator, num2):
    if type(num1) is int and type(num2) is int:

        compute(num1, operator, num2)
    else:
        print("Les paramètres 1 et 3 de la fonction add doivent être des nombres !")


def compute(num1, operator, num2):

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "%":
        print(num1 % num2)
    else:
        print("Ce que vous avez renseigné comme operateur n'est pas valide")


calcul(4, "/", 5)


