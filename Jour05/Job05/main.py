# Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont au
# rez-de-chaussée...
# Écrire une fonction qui reçoit en paramètres, le nombre de marches du phare et la
# hauteur de chaque marche (en cm), cette fonction doit calculer combien de mètre le
# gardien effectué par semaine pour aller aux toilettes. La sortie du code doit être :
# Pour x marches de y cm, le gardien parcours z.zz m par semaine.
# On n'oubliera pas :
# qu'une semaine comporte 7 jours ;
# qu'une fois en bas, le gardien doit remonter ;
# que le résultat est à exprimer en m.

def count_meters(stairs,height):
    z = 7 * (5 * (stairs * height) * 2)
    z_in_meter = z / 100
    x = (str(stairs))
    y = (str(height))
    z_in_meter = (str(z_in_meter))
    print("Pour " + x + " marches de " + y + " cm, le gardien parcours " + z_in_meter + " m par semaine.")

count_meters(1,20)