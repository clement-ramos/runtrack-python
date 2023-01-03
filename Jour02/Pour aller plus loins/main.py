import cmath
import math
def triangle_tester(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        print("Construire un triangle avec ces mesures est possible")

        if a == b == c:
            print("Ce triangle est équilatéral")

        elif a == b or b == c or c == a:
            print("Ce triangle est isocèle")
            if is_rectangle(a, b, c):
                print("et rectangle")

        elif is_rectangle(a, b, c):
            print("Ce triangle est rectangle")


        else:
            print("Ce triangle est quelquonque")

    else:
        print("Il n'est pas possible de construire un triangle")


def is_rectangle(a, b, c):
    rectangle = a * a + b * b == c * c or c * c + b * b == a * a or a * a + c * c == b * b
    return rectangle



triangle_tester(4, 5, 2)
triangle_tester(2, 5, 2)
triangle_tester(9, 15, 12)
triangle_tester(4, 4, 4)
triangle_tester(4, 4, 5)

third = math.sqrt(35.28)

triangle_tester(4.2, 4.2, third)