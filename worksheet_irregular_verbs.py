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
numberOfWorksheets = 30
while worksheetNumber <= numberOfWorksheets:
    title = 'Irregular Verbs Worksheet ' + str(worksheetNumber) + " - Date :"
    # Add page to the PDF
    pdf.add_page()

    # Set the header for the PDF file
    pdf.set_font('Arial', 'B', size = 16)
    pdf.cell(0, 15, txt=title, ln=1, align='C')

    pdf.set_font('Arial', 'I', size = 11)
    pdf.cell(0, 5, txt='Remplir les champs manquants et donner la traduction des verbes.', ln=1, align='C')
    pdf.cell(0, 6, txt='De gauche à droite : base verbale - prétérit - participe passé - traduction', ln=1, align='C')


    pdf.set_font('Arial', size = 11)
    # Generate the answer rows with only one clue chosen at random
    indices = list(range(len(verbs)))
    numberOfVerbs = 20      # Define the number of verbs to work on

    for i in range(numberOfVerbs):
        guessLine = 4*[' '*35]
        verbIndex = indices[random.randint(0, len(indices)-1)]
        indices.remove(verbIndex) # Make sure we don't get the same verb more than once
        formIndex = random.randint(0, len(verbs[0])-1)
        guessLine[formIndex] = verbs[verbIndex][formIndex]

        # Generate the PDF cells/table containing the exercise
        b = 47
        for i in range(len(guessLine)):
            if i < 3:
                pdf.cell(b, 12, txt=guessLine[i], ln=0, border=1, align='C')
            else:
                pdf.cell(b, 12, txt=guessLine[i], ln=1, border=1, align='C')

    # Increment the worksheet number
    worksheetNumber += 1

# Generate the PDF
pdf.output("IVW.pdf")
