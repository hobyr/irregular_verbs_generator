#! /usr/bin/env python3
'''
Main module holding the main function for the program.
# main.py -- Generator of irregular verbs worksheets
'''
import sys
from fpdf import FPDF # To generate the PDFs of the worksheets

import irregular_verbs_create

@irregular_verbs_create.performance
def main():
    '''Main function.

    Generates a PDF file of specified pages containing
    exercises and answers for practicing English irregular verbs.
    '''
    if len(sys.argv) < 2:
        print('Usage: createIVWenglish [verb list file] '
              '[start worksheet no.] [no. of worksheets]'
              ' [output PDF file]')
        sys.exit()

    list_file = sys.argv[1]
    worksheet_number = int(sys.argv[2])
    number_of_worksheets = int(sys.argv[3])
    output_pdf_file = sys.argv[4]

    # Import the verbs list into a suitable array
    verbs = irregular_verbs_create.import_verbs(list_file)

    pdf = FPDF() # Generate PDF master file

    while worksheet_number <= number_of_worksheets:
        title_student = 'Irregular Verbs Worksheet ' + \
            str(worksheet_number) + " - Date :"
        title_teacher = 'Irregular Verbs Worksheet ' + \
            str(worksheet_number) + " - Correction"

        # Generate the table for test/answers
        test, answers, form_indices = irregular_verbs_create.generate_tables(verbs)
        #------------------------------------------
        # 1. TEST SHEET
        #------------------------------------------

        # Add page to the PDF that is the test page
        pdf.add_page()

        # Set the header for the test sheet
        irregular_verbs_create.set_header(pdf, title_student, 'test')

        # Generate the PDF page containing the exercise
        pdf.set_font('Arial', size=11)
        for line in test:
            for value in line:
                pdf.cell(48, 12, txt=value, ln=0, border=1, align='C')
            pdf.ln()

        #------------------------------------------
        # 2. ANSWER SHEET
        #------------------------------------------

        # Add page to the PDF that is the correction page
        pdf.add_page()

        # Set the header for the correction sheet
        irregular_verbs_create.set_header(pdf, title_teacher, 'correction')

        # Generate the table containing the answers
        j = 0
        for line in answers:
            i = 0
            for value in line:
                if i == form_indices[j]:
                    pdf.set_font('Arial', 'IB', size=11)
                else:
                    pdf.set_font('Arial', size=11)
                pdf.cell(48, 12, txt=value, ln=0, border=1, align='C')
                i += 1
            j += 1
            pdf.ln()

        # Increment the worksheet number
        worksheet_number += 1

    # Generate the PDF
    pdf.output(output_pdf_file)

if __name__ == "__main__":
    main()
