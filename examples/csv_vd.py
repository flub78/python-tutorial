#!/usr/bin/python
# -*- coding:utf8 -*

import sys
import csv
import os
import re  

if len(sys.argv) <= 2:
    print("Please provide a CSV input and result file, args=", len(sys.argv))
    sys.exit(1)

# Fonction pour convertir une date du format JJ/MM/YY vers YYYY-MM-DD
def convert_date(date_str):
    if not date_str or date_str.strip() == '':
        return ''
    
    # Nettoyer la chaîne date
    date_str = date_str.strip()
    
    # Gérer les formats erronés
    if '/' not in date_str:
        # Tenter de détecter un format comme '26/036' (erreur dans le CSV original)
        if re.match(r'\d{2}/\d{3}', date_str):
            day, month_year = date_str.split('/')
            month = month_year[:2]
            year = '20' + month_year[2:]
            date_str = f"{day}/{month}/{year}"
    
    try:
        # Gérer différents formats possibles
        if re.match(r'\d{2}/\d{2}/\d{2}', date_str):  # Format JJ/MM/YY
            day, month, year = date_str.split('/')
            year = '20' + year if len(year) == 2 else year
            return f"{year}-{month}-{day}"
        elif re.match(r'\d{2}/\d{2}/\d{4}', date_str):  # Format JJ/MM/YYYY
            day, month, year = date_str.split('/')
            return f"{year}-{month}-{day}"
        else:
            print(f"Format de date non reconnu: {date_str}")
            return ''
    except Exception as e:
        print(f"Erreur lors de la conversion de la date {date_str}: {e}")
        return ''
    
# declare a dictionary to store the results
data = {}
sections = {}
cvs_data = []
filename = sys.argv[1]
result_file = sys.argv[2]

headers = ['n°', 'opérateur', 'Date de vente', 'Type de vol', 'Prix', 'mode règle,', 'Bénéficiaire', 'N° à contacter', 'Nb personnes', 'Date du vol', 'Appareil', 'Pilote', '', '', '', '', '', '']
fieldnames = [
            'id', 'saisie_par', 'date_vente', 'club', 'product', 'beneficiaire',
            'de_la_part', 'occasion', 'paiement', 'participation', 'beneficiaire_email',
            'beneficiaire_tel', 'urgence', 'date_planning', 'time_planning',
            'date_vol', 'time_vol', 'pilote', 'airplane_immat', 'cancelled',
            'nb_personnes', 'prix'
        ]
cvs_data.append(fieldnames)

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    line = 0
    for row in csv_reader:

        if line == 0:      # headers line
            # continue
            pass
            print("header: ", row)
            
        line = line + 1

        fld = 0
        new_row = []
        for header in headers:
            value = row[fld]

            if header == "Date de vente":
                value = convert_date(value)
            elif header == "Date du vol":
                value = convert_date(value)

            new_row.append(value)
            print(header, ": ", new_row[fld])
            fld += 1
        cvs_data.append(new_row)

    # Generate output CSV filename by adding _uniq to the basename of the input CSV
    output_csv_path = os.path.splitext(filename)[0] + '_uniq.csv'
    output_csv_path = result_file

    if cvs_data:
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in cvs_data:  # Using the first table as an example
                writer.writerow(row)