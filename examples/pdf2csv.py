#!/usr/bin/python
# -*- coding:utf8 -*

import sys

if len(sys.argv) != 2:
    print("Usage: python pdf2csv.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
print(f"pdf2csv file: {filename}")

# Function to check if all words from a string are in the line
def contains_all_words(line, skip_str):
    skip_words = skip_str.lower().split()
    line_words = line.lower().split()
    return all(word in line_words for word in skip_words)

def parse(filename):
    """
    Process a text file line by line.

    This function opens a text file and prints each line after removing leading/trailing whitespace.

    Args:
        filename (str): The path to the file to be processed.

    Returns:
        A hash map of processed lines.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
        IOError: If there is an error reading the file.
    """

    # Initialize a hash map to store the results
    result = {}
    
    # Define an array of strings to skip
    skip_strings = ['Votre Banque à Distance',
                    'Internet : entreprises.sg.fr', 
                    'Votre compte est éligible à la garantie du Fonds de Garantie des Dépôts et de Résolution selon',
                    'Opération exonérée de commission de mouvement',
                    'VOS CONTACTS',
                    'Courrier : 21 PL MAX LEJEUNE', "Service d'urgence 24 h/24",
                    "Perte ou vol de vos cartes / chèques", "Société Générale                           552 120 222 RCS Paris",
                    "S.A. au capital de 1 003 724 927,50 Eur    Siège Social",
                    "N° ADEME : FR231725_01YSGB", 
                    "29, bd Haussmann 75009 Paris", 
                    "Pour toute insatisfaction ou désaccord, vous pouvez contacter",
                    "1 - L'agence : votre premier interlocuteur",
                    "2 - Le Service Relations Clientèle : Adresse",
                    "3 - Le Médiateur : En dernier recours, gratuitement, le Médiateur de la FBF",
                    "SG-SocieteGenerale.Reclamations@socgen.com",
                    "RA423319",
                    "Conditions générales du service de la médiation consommateurs",
                    "75422 PARIS CEDEX 09 ou sur le site lemediateur.fbf.fr ou sur",
                    "suite >>>"]

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
 
            # Skip empty lines
            if not line:
                continue

            result['operations'] = []
            current_operation = None

            # Skip the line if it contains all words from any of the skip strings
            if any(contains_all_words(line, skip_str) for skip_str in skip_strings):
                continue

            if line.startswith("Votre agence "):
                result['bank'] = line[len("Votre agence "):]
                continue

            if line.startswith("COMPTE D'ADMINISTRATION - en "):
                result['currency'] = line[len("COMPTE D'ADMINISTRATION - en "):]
                continue

            if line.startswith("n° "):
                result['iban'] = line[len("n° "):]
                continue

            if line.startswith("Téléphone : 03 22 25 30 68"):
                result['section'] = line[len("Téléphone : 03 22 25 30 68"):].strip()
                continue

            if "SOLDE PRÉCÉDENT AU" in line:
                parts = line.strip().split()
                try:
                    result['previous_balance_date'] = parts[3]
                    # Convert amount string (e.g., "14.575,02") to float
                    amount = parts[-1].replace('.', '').replace(',', '.')
                    result['previous_balance'] = float(amount)
                except (IndexError, ValueError):
                    pass

            # Check for operation lines with dates and FACTURATION
            if len(line.split()) >= 4:
                parts = line.split()
                try:
                    # Check if first two elements are dates in format DD/MM/YYYY
                    if '/' in parts[0] and '/' in parts[1]:
                        amount = parts[-1].replace(',', '.')
                        if amount.replace('.', '').isdigit():
                            current_operation = {
                                'date': parts[0],
                                'value_date': parts[1],
                                'nature': ' '.join(parts[2:-1]).strip(),
                                'amount': float(amount)
                            }
                            result['operations'].append(current_operation)
                except (IndexError, ValueError):
                    pass
                continue
            print(f"Unprocessed line: {line}")

    return result

parsed_data = parse(filename)
print("\nParsed data:")
for key, value in parsed_data.items():
    print(f"{key}: {value}")
print("end")

