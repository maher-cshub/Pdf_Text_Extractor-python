
# importing required modules
from PyPDF2 import PdfReader
  
# creating a pdf reader object
reader = PdfReader('target.pdf')
  
cpt = 0
for page in reader.pages:
    cpt += 1
    # extracting text from page
    text = page.extract_text()
    new_file = open(f"page_{cpt}.txt",'w',encoding="utf-8")
    new_file.write(text)
    new_file.close()

    