#!/usr/bin/python

import math

def alunissage():
    # Constantes
    gravite_lunaire = 1.625  # m/s^2 (gravité sur la Lune)
    impulsion_moteur = 1.2  # m/s^2 (poussée du moteur)

    # Variables initiales
    altitude = 100.0  # m (altitude initiale)
    vitesse_verticale = 0.0  # m/s

    # Boucle de simulation
    while altitude > 0:
        # Affichage de l'état actuel
        print("Altitude:", round(altitude, 2), "m, Vitesse verticale:", round(vitesse_verticale, 2), "m/s")

        # Saisie de la quantité de carburant brûlé par le joueur
        carburant_brule = float(input("Entrez la quantité de carburant brûlé (0 pour aucun) : "))

        # Calcul de la poussée du moteur
        poussée = 0.0
        if carburant_brule > 0:
            poussée = carburant_brule # min(carburant_brule, impulsion_moteur)
            carburant_brule -= poussée

        # Calcul de la gravité
        gravite = gravite_lunaire

        # Mise à jour de la vitesse et de l'altitude
        vitesse_verticale += (gravite - poussée)
        altitude -= vitesse_verticale

        # Vérification des conditions de victoire
        if altitude <= 0 and vitesse_verticale < 2:
            print("\nAtterrissage réussi! Altitude:", round(altitude, 2), "m, Vitesse verticale:", round(vitesse_verticale, 2), "m/s")
            return

    # Si la boucle se termine sans condition de victoire
    print("\nAtterrissage échoué. Altitude:", round(altitude, 2), "m, Vitesse verticale:", round(vitesse_verticale, 2), "m/s")

# Appel de la fonction pour démarrer la simulation
alunissage()
