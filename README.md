# Generator of worksheets for English Irregular Verbs

This is a Python generator for worksheets about English Irregular Verbs.
It generates a PDF page with a table of 20 lines, with a clue about the verb to guess.

Each line is unique, and the clue is positioned randomly in the table.
In the code, it's possible to specify the number of worksheets to generate.

Each table is randomly generated, so it's very rare that you'll get the exact same table twice, even if you generate thousands of worksheets.

### IVW.pdf

The given PDF file is an example of how the generated worksheets look.
It contains 3 worksheets + their corrections ready to be used.
The instructions at the top of the page, aimed at students, is currently written in French. Get into the code to modify it into the desired language.

### Versions

v1.2: Refactored code for scalability, cleanliness and performance. Generated 200 pages in ~1.5s (2010 Macbook A1342)  
v1.1: Added correction sheet functionality.  
v1.0: Initial version.
