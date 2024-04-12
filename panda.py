import pandas as pd
from docx import Document
import json


d = pd.read_excel(r'Name.xlsx', sheet_name = "List")
print(d)

doc = Document('Hello.docx')
pars = doc.paragraphs[0].text
print(pars)