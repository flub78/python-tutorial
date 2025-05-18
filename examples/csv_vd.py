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

in_headers = ['n°', 'opérateur', 'Date de vente', 'Type de vol', 'Prix', 'mode règle,', 'Bénéficiaire', 'N° à contacter', 'Nb personnes', 'Date du vol', 'Appareil', 'Pilote', '', '', '', '', '', '']

out_headers = [
            'id', 'saisie_par', 'date_vente', 'club', 'product', 'beneficiaire',
            'de_la_part', 'occasion', 'paiement', 'participation', 'beneficiaire_email',
            'beneficiaire_tel', 'urgence', 'date_planning', 'time_planning',
            'date_vol', 'time_vol', 'pilote', 'airplane_immat', 'cancelled',
            'nb_personnes', 'prix'
        ]

def club(row):
    prd = product(row)

    if prd == "planeur":
        return 1
    if "ulm" in prd:
        return 2
    return 3

def beneficiaire(row):
    res = row[6].title()
    return res

def paiement(row):
    res = row[5]
    return res

def cancelled(row):
    for element in row:
        if isinstance(element, str) and 'annul' in element.lower():
            return 1
    return 0

'''
abbeville
baie
falaises
planeur
abbeville_ulm
baie_ulm
falaises_ulm
''' 
def product(row):
    product = row[3]
    if product.lower().strip()=='planeur' or product.lower().strip()=='vv':
            return 'planeur' 
    if "BS" in product.upper():
        product = "baie"
    elif "FAL" in product.upper():
        product = "falaises"
    elif "ABB" in product.upper():
        product = "abbeville"
    elif product.upper() == "ULM":
        product = "baie"
    else:
        product = "unknow product |" + product + "|"

    if 'ULM' in row[3].upper():
        product += "_ulm"
          
    return product

def convert_row(row):
    print("")
    nr = []

    nr.append( row[0])
    nr.append( row[1])
    nr.append( convert_date(row[2]))
    nr.append( club(row))
    nr.append( product(row))
    nr.append( beneficiaire(row))
    nr.append( "")      # de la part
    nr.append( "")      # occasion
    nr.append( paiement(row))
    nr.append( "")   # participation
    nr.append( "")   # email
    nr.append( "")   # tel
    nr.append( row[7])   # urgence
    nr.append( "")   # date planning
    nr.append( "")   # time planning
    nr.append( convert_date(row[9])) # date vol
    nr.append( "")   # time vol
    nr.append( row[11])   # pilote
    nr.append( row[10])   # immat
    nr.append( cancelled(row))  
    nr.append( row[8])   # nb pers
    nr.append( row[4])   # prix

    i = 0;
    for fld in nr:
        print (out_headers[i], nr[i])
        i += 1
    return nr

# declare a dictionary to store the results
data = {}
sections = {}
cvs_data = []
filename = sys.argv[1]
result_file = sys.argv[2]

cvs_data.append(out_headers)

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    line = 0
    for row in csv_reader:

        if line == 0:      # headers line
            # continue
            pass
            print("header: ", row)
        else:
            cvs_data.append(convert_row(row))
            
        line = line + 1

    # Generate output CSV filename by adding _uniq to the basename of the input CSV
    output_csv_path = os.path.splitext(filename)[0] + '_uniq.csv'
    output_csv_path = result_file

    if cvs_data:
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in cvs_data:  # Using the first table as an example
                writer.writerow(row)