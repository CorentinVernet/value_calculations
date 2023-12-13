# Choix du calcul
choice_1 = float(input("Entrez votre choix de calcul : \n1 : Caluler des Ohms.\n2 : Calculer des Volts. \n3 : Calculer des Ampères.\n4 : Entrer les couleurs des bagues des résistances.\n5 : Calculer des resistances en serie ou en paralèlle.\n"))

if choice_1 == 1:
    # Calculer résistance (ohms)
    u1 = float(input("Entrez votre valeur en Volts : "))
    i1 = float(input("Entrez votre valeur en Ampères : "))
    r1 = u1/i1
    print(r1, "ohms")

if choice_1 == 2:
    # Calculer tension (volts)
    r2 = float(input("Entrez votre valeur en Ohms : "))
    i2 = float(input("Entrez votre valeur en Ampères : "))
    u2 = r2*i2
    print(u2, "volts")

if choice_1 == 3:
    # Calculer intensité (ampères)
    u3 = float(input("Entrez votre valeur en Volts : "))
    r3 = float(input("Entrez votre valeur en Ohms : "))
    i3 = u3/r3
    print(i3, "ampères")

if choice_1 == 4:

    # Définition des couleurs + valeurs
    couleurs = {
    "noir": 0, "marron": 1, "rouge": 2, "orange": 3, "jaune": 4,
    "vert": 5, "bleu": 6, "violet": 7, "gris": 8, "blanc": 9
    }

    multiplicateurs = {
    "noir": 1, "marron": 10, "rouge": 100, "orange": 1000, "jaune": 10000,
    "vert": 100000, "bleu": 1000000
    }

    # Calculer la valeur de la résistance
    def calculer_resistance(couleur1, couleur2, couleur3):
        valeur = (couleurs[couleur1] * 10 + couleurs[couleur2]) * multiplicateurs[couleur3]
        return valeur


    # Input pour entrer les couleurs des bagues
    couleur1 = input("Entrez la couleur de la première bague: ").lower()
    couleur2 = input("Entrez la couleur de la deuxième bague: ").lower()
    couleur3 = input("Entrez la couleur de la troisième bague: ").lower()


    # Vérifie si les couleurs saisies sont valides
    if couleur1 in couleurs and couleur2 in couleurs and couleur3 in multiplicateurs:
        resistance = calculer_resistance(couleur1, couleur2, couleur3)
        print("La valeur de la résistance est de", resistance, "ohms")
    else:
        print("Couleurs invalides. Assurez-vous d'entrer des couleurs valides pour les bagues.")

if choice_1 == 5:
    # Choix resistance calcule
    choice_2 = float(input("Choix du calcule. \n1 : Calculer des resistances en serie. \n2 : Calculer resistances en parallele. \n"))

    # En serie
    if choice_2 == 1:
        resistances_en_serie = []

        while True:
            resistance_value = float(input("Entrez la valeur de votre résistance (ou tapez 'exit') : "))
            resistances_en_serie.append(resistance_value)

            # Vérifie si au moins deux résistances ont été entrés
            if len(resistances_en_serie) >= 2:
                user_input = input("Entrez 'more' s'il y a plus de résistances, sinon tapez 'exit' :\n")
                if user_input.lower() == 'exit':
                    break
            else:
                print("Vous devez entrer au moins deux résistances.")

        total_resistance_serie = sum(resistances_en_serie)
        print(f,"La résistance totale en série est de {total_resistance_serie} ohms.")

    # En parallele
    elif choice_2 == 2:
        resistances_en_parallele = []

        # Première résistance en parallèle
        resistance_value = float(input("Entrez la valeur de votre première résistance en parallèle (ou tapez 'exit') : "))
        resistances_en_parallele.append(resistance_value)

        while True:
            user_input = input("Entrez 'more' s'il y a plus de résistances en parallèle, sinon tapez 'exit' :\n")
            if user_input.lower() == 'exit':
                break

            resistance_value = float(input("Entrez la valeur de votre résistance en parallèle (ou tapez 'exit') : "))
            resistances_en_parallele.append(resistance_value)

        total_resistance_parallele = 1 / sum(1 / r for r in resistances_en_parallele)
        print(f,"La résistance totale en parallèle est de {total_resistance_parallele} ohms.")