# Step 1: Unzipping the File

import shutil
import re
import os

shutil.unpack_archive('unzip_me_for_instructions.zip')

# Step 2: Read the instructions file

with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

# Step 3: Regular Expression to Find the Link

pattern = r'\d{3}-\d{3}-\d{4}'
test_string = "here is a random number 1231231234 , here is phone number formatted 123-123-1234"

print(re.findall(pattern,test_string))

# Step 4: Create a function for regex

def search(file,pattern= r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''
    
# Step 5: OS Walk through the Files to Get the Link
    
results = []
for folder , sub_folders , files in os.walk(os.getcwd()+"\\extracted_content"):
    
    for f in files:
        full_path = folder+'\\'+f
         
        results.append(search(full_path)) 

for r in results:
    if r != '':
        print(r.group())