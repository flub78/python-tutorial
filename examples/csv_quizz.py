#!/usr/bin/python
# -*- coding:utf8 -*

import sys
import csv
import os

if len(sys.argv) <= 1:
    print("Please provide a CSV file argument, args=", len(sys.argv))
    sys.exit(1)

# declare a dictionary to store the results
data = {}
sections = {}
cvs_data = []
cvs_data.append(["Id", "Question", "", "Réponse 1", "Réponse 2", "Réponse 3", "Réponse 4", "Correct", "Required", "Points", "Type"]) 
filename = sys.argv[1]

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if row[0] == "Id":      # skip the headers
            continue
        if row[10] == "SECTION":
            section = row[1]
            if section not in data:
                data[section] = {}
                sections[section] = row
            continue
        else:
            # regular question
            id = row[0]
            data[section][id] = row

    # for all sections in data
    for section in data:
        cvs_data.append(sections[section])

        # push all questions in csv_result
        for id in data[section]:
            cvs_data.append(data[section][id])

    # Generate output CSV filename by adding _uniq to the basename of the input CSV
    output_csv_path = os.path.splitext(filename)[0] + '_uniq.csv'

    if cvs_data:
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in cvs_data:  # Using the first table as an example
                writer.writerow(row)