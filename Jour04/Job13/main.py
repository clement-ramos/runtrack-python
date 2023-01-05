L = [10,20,30,20,10,50,60,40,80,50,40]

#Méthode du chomeur:

#print(L)
#sans_doublons = list(set(L))
#print(sans_doublons)

#Autre méthode:

def doublon_check(list):

    sans_doublons = []
    for element in list:
        if element not in sans_doublons:
            sans_doublons += [element]
    # imprimer le résultat
    print(sans_doublons)


doublon_check(L)
