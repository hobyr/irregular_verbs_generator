#! python3
# worksheet_irregular_verbs.py -- Generator of irregular verbs worksheets
import random
from fpdf import FPDF # To generate the PDFs of the worksheets

pdf = FPDF()

# Import the verbs list into a suitable array
file = open('irregular_verbs_list.csv', 'r')
file.seek(53)
verbs = []
for line in file:
    verbs.append(line[:-2].split(' ,'))
file.close()

# Define the number of worksheets to generate
worksheetNumber = 1
numberOfWorksheets = 3
while worksheetNumber <= numberOfWorksheets:
    title_student = 'Irregular Verbs Worksheet ' + str(worksheetNumber) + " - Date :"
    title_teacher = 'Irregular Verbs Worksheet ' + str(worksheetNumber) + " - Correction"

    # Add page to the PDF that is the student page
    pdf.add_page()

    # Set the header for the PDF file
    pdf.set_font('Arial', 'B', size = 16)
    pdf.cell(0, 15, txt=title_student, ln=1, align='C')

    pdf.set_font('Arial', 'I', size = 11)
    pdf.cell(0, 5, txt='Remplir les champs manquants et donner la traduction des verbes.', ln=1, align='C')
    pdf.cell(0, 6, txt='De gauche à droite : base verbale - prétérit - participe passé - traduction', ln=1, align='C')


    pdf.set_font('Arial', size = 11)
    # Generate the answer rows with only one clue chosen at random
    indices = list(range(len(verbs)))
    numberOfVerbs = 20      # Define the number of verbs to work on
    verbIndicesList = []
    formIndicesList = []
    for i in range(numberOfVerbs):
        x = indices[random.randint(0, len(indices)-1)]
        verbIndicesList.append(x)
        indices.remove(x) # Make sure we don't get the same verb more than once

    for verbIndex in verbIndicesList:
        guessLine = 4*[' '*35]
        formIndex = random.randint(0, len(verbs[0])-1)
        formIndicesList.append(formIndex)
        guessLine[formIndex] = verbs[verbIndex][formIndex]

        # Generate the PDF cells/table containing the exercise
        b = 47
        for i in range(len(guessLine)):
            if i < 3:
                pdf.cell(b, 12, txt=guessLine[i], ln=0, border=1, align='C')
            else:
                pdf.cell(b, 12, txt=guessLine[i], ln=1, border=1, align='C')

    # Add page to the PDF that is the correction page
    pdf.add_page()

    # Set the header for the PDF file
    pdf.set_font('Arial', 'B', size = 16)
    pdf.cell(0, 15, txt=title_teacher, ln=1, align='C')

    pdf.set_font('Arial', size = 11)
    j=0
    for verbIndex in verbIndicesList:
        answerLine = verbs[verbIndex]
        form = formIndicesList[j]
        j += 1

        # Generate the PDF cells/table containing the exercise
        b = 47
        for i in range(len(answerLine)):
            if i == form:
                pdf.set_font('Arial', 'IB', size = 11)
            else:
                pdf.set_font('Arial', size = 11)
            if i < 3:
                pdf.cell(b, 12, txt=answerLine[i], ln=0, border=1, align='C')
            else:
                pdf.cell(b, 12, txt=answerLine[i], ln=1, border=1, align='C')

    # Increment the worksheet number
    worksheetNumber += 1

# Generate the PDF
pdf.output("IVW.pdf")
