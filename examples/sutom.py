#!/usr/bin/env python3
import sys
import math
from collections import defaultdict

def charger_dictionnaire(fichier, premiere_lettre, longueur):
    """Charge les mots du dictionnaire correspondant aux critères"""
    mots = []
    with open(fichier, 'r', encoding='utf-8') as f:
        for ligne in f:
            mot = ligne.strip().upper()
            if len(mot) == longueur and mot[0] == premiere_lettre:
                mots.append(mot)
    return mots

def generer_pattern(mot_test, mot_solution):
    """Génère le pattern de réponse pour un mot test vs une solution"""
    pattern = ['_'] * len(mot_test)
    lettres_solution = list(mot_solution)
    
    # D'abord les bien placées
    for i in range(len(mot_test)):
        if mot_test[i] == mot_solution[i]:
            pattern[i] = '='
            lettres_solution[i] = None
    
    # Puis les mal placées
    for i in range(len(mot_test)):
        if pattern[i] == '_' and mot_test[i] in lettres_solution:
            pattern[i] = '?'
            lettres_solution[lettres_solution.index(mot_test[i])] = None
    
    return ''.join(pattern)

def calculer_entropie(mot_test, candidats):
    """Calcule l'entropie d'un mot test sur les candidats restants"""
    partitions = defaultdict(list)
    for candidat in candidats:
        pattern = generer_pattern(mot_test, candidat)
        partitions[pattern].append(candidat)
    
    entropie = 0
    n = len(candidats)
    for groupe in partitions.values():
        p = len(groupe) / n
        entropie -= p * math.log2(p) if p > 0 else 0
    return entropie

def meilleur_mot(candidats):
    """Trouve le mot avec la meilleure entropie"""
    if len(candidats) == 1:
        return candidats[0]
    
    meilleur = None
    max_entropie = -1
    
    for mot in candidats:
        entropie = calculer_entropie(mot, candidats)
        if entropie > max_entropie:
            max_entropie = entropie
            meilleur = mot
    
    return meilleur

def saisir_reponse(mot):
    """Interface pour saisir la réponse"""
    print(f"\nMot proposé : {mot}")
    print("Pour chaque position, indiquez :")
    print("  <lettre> ou = : lettre correcte et bien placée")
    print("  ? : lettre correcte mais mal placée")
    print("  _ : lettre incorrecte")
    print(f"\nEntrez la réponse complète ({len(mot)} caractères) :")
    
    while True:
        r = input(f"  Réponse [{mot}] : ").strip().upper()
        
        if len(r) != len(mot):
            print(f"    Erreur : la réponse doit contenir exactement {len(mot)} caractères")
            continue
        
        # Convertir les lettres en =
        reponse = ""
        valide = True
        for i, c in enumerate(r):
            if c == mot[i]:
                reponse += '='
            elif c in ['=', '?', '_']:
                reponse += c
            else:
                print(f"    Erreur : caractère invalide '{c}' à la position {i+1}")
                print(f"    Utilisez =, ?, _ ou la lettre {mot[i]}")
                valide = False
                break
        
        if valide:
            return reponse

def filtrer_candidats(candidats, mot_test, reponse):
    """Filtre les candidats selon la réponse reçue"""
    return [c for c in candidats if generer_pattern(mot_test, c) == reponse]

def main():
    if len(sys.argv) != 2:
        print("Usage: python motus.py <fichier_dictionnaire>")
        sys.exit(1)
    
    fichier_dict = sys.argv[1]
    
    # Initialisation
    premiere_lettre = input("Première lettre du mot : ").strip().upper()
    longueur = int(input("Nombre de lettres : "))
    
    candidats = charger_dictionnaire(fichier_dict, premiere_lettre, longueur)
    print(f"\n{len(candidats)} mots possibles trouvés")
    
    if len(candidats) == 0:
        print("Aucun mot correspondant dans le dictionnaire!")
        return
    
    # Boucle de jeu
    essai = 0
    while len(candidats) > 0:
        essai += 1
        mot_propose = meilleur_mot(candidats)
        
        print(f"\n--- Essai {essai} ---")
        print(f"Candidats restants : {len(candidats)}")
        
        reponse = saisir_reponse(mot_propose)
        
        # Vérifier si gagné
        if reponse == '=' * longueur:
            print(f"\n🎉 Mot trouvé en {essai} essai(s) : {mot_propose}")
            break
        
        # Filtrer
        candidats = filtrer_candidats(candidats, mot_propose, reponse)
        
        if len(candidats) == 0:
            print("\n❌ Aucun mot ne correspond. Erreur de saisie?")
            break

if __name__ == "__main__":
    main()