# Task One: Grab the Google Drive link from .csv file.

import csv

data = open('find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

# Method 1

link_list = []
for row_num,data in enumerate(data_lines):
    link_list.append(data[row_num])
print(''.join(link_list))

# Method 2

link_str = ''
for row_num,data in enumerate(data_lines):
    link_str+=data[row_num]
print(link_str)    


# Task Two: Download the PDF from the Google Drive link and 
#Find the phone number that is in the document. 

import PyPDF2
f = open('Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfReader(f)
print(len(pdf.pages))

# Phone Number Matching

import re
pattern = r'\d{3}'
all_text = ''

for n in range(len(pdf.pages)):
    page = pdf.pages[n]
    page_text = page.extract_text()
    all_text = all_text+' '+page_text

for match in re.finditer(pattern,all_text):
    print(match)

import re
pattern = r'\d{3}.\d{3}.\d{4}' 

for n in range(len(pdf.pages)):    
    page  = pdf.pages[n]
    page_text = page.extract_text()
    match = re.search(pattern,page_text)
    
    if match:
        print(match.group())