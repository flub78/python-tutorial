#!/usr/bin/env python
# coding: utf-8
# Extract formulas from an ODS file using odfpy
import sys
import re
from odf import opendocument
from odf.table import Table, TableRow, TableCell

def column_index_to_letter(index):
    """Convert column index (0-based) to Excel-style letter (A, B, ..., Z, AA, AB, ...)"""
    result = ""
    index += 1  # Convert to 1-based
    while index > 0:
        index -= 1
        result = chr(65 + (index % 26)) + result
        index //= 26
    return result

def extract_cell_references(formula):
    """Extract all cell references from a formula (e.g., A1, B2, Sheet1.A1)"""
    # Pattern to match cell references like A1, B2, Sheet1.A1, [Sheet1.A1]
    pattern = r'\[?(?:[\w]+\.)?([A-Z]+\d+)\]?'
    matches = re.findall(pattern, formula)
    return set(matches)

if len(sys.argv) < 2 or '--help' in sys.argv or '-h' in sys.argv:
    print("Extract formulas from an ODS file")
    print()
    print("This script reads an ODS file and extracts all cells containing formulas,")
    print("displaying their coordinates and formula content.")
    print()
    print("Usage: python extract_formulas.py [OPTIONS] <ods_file>")
    print()
    print("Arguments:")
    print("  <ods_file>      Path to the ODS file (.ods)")
    print()
    print("Options:")
    print("  -h, --help      Show this help message and exit")
    print("  --ref           Show only cells that are referenced in formulas")
    sys.exit(0 if '--help' in sys.argv or '-h' in sys.argv else 1)

# Parse command line arguments
show_ref_only = '--ref' in sys.argv
filename = [arg for arg in sys.argv[1:] if not arg.startswith('-')][0]

doc = opendocument.load(filename)

# Get all sheets
sheets = doc.spreadsheet.getElementsByType(Table)

# First pass: collect all formulas and referenced cells if --ref is active
all_formulas = []
referenced_cells = set()

for sheet in sheets:
    sheet_name = sheet.getAttribute('name')
    rows = sheet.getElementsByType(TableRow)

    for row_index, row in enumerate(rows):
        cells = row.getElementsByType(TableCell)
        col_index = 0

        for cell in cells:
            # Handle repeated columns
            repeat = cell.getAttribute('numbercolumnsrepeated')
            repeat = int(repeat) if repeat else 1

            # Check if cell has a formula
            formula = cell.getAttribute('formula')
            if formula:
                # Convert to Excel-style coordinate (A1, B2, etc.)
                col_letter = column_index_to_letter(col_index)
                coordinate = f"{col_letter}{row_index + 1}"
                full_coordinate = f"{sheet_name}!{coordinate}"

                all_formulas.append((full_coordinate, formula))

                # Extract cell references from the formula
                if show_ref_only:
                    refs = extract_cell_references(formula)
                    referenced_cells.update(refs)

            col_index += repeat

# Second pass: display results
if show_ref_only:
    # Display only cells that are referenced in formulas
    print("Cells referenced in formulas:")
    for ref in sorted(referenced_cells):
        print(f"  {ref}")
else:
    # Display all formulas
    for coordinate, formula in all_formulas:
        print(f"{coordinate}: {formula}")