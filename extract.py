import sys

from PyPDF2 import PdfReader
import re, json

pdf = PdfReader("resume.pdf")
text_data = ""
NumOfPages = len(pdf.pages)
for i in range(NumOfPages):
    page = pdf.pages[i]
    text_data += page.extract_text()

words = re.findall(r"[A-Z].*", text_data)
name = re.findall(r"B\.\w[^\n]*", text_data)[0]
email = (re.findall(r"[\@\w\.][^\|\-]*gmail.com", text_data)[0]).replace(" ", "")
phoneNumber = int(re.findall(r"\d{10}", text_data)[0])
address = re.findall(r"Mac[\w\,\s]*", text_data)[0].strip()

skill1 = re.findall(r"HTML\,\w*[\,\s]*\w*[^\n]+", text_data)[0]
skill2 = re.findall(r"Pyth\w*[\,\s]*\w*[^\n]+", text_data)[0]
skill3 = re.findall(r"SQ\w", text_data)[0]
skills1 = [skill1, skill2, skill3]
skills = []
for w in skills1:
    word = (w.replace(" ", "")).split(",")
    skills.extend(word)
# print(skills)

higherEducation = (re.findall(r"Po[\w\-\(\)\s\.]+", text_data)[0]).split(" - ")
qualification = higherEducation[0]
collegeGrade = higherEducation[1].split(" \n")
collegeName = collegeGrade[1]
grade = collegeGrade[0].strip()
passedOut = re.findall(r"M\w{2}, \d{4}", text_data)[0]

education = {"collegeName": collegeName, "grade": grade,  "qualification": qualification, "passedOut":passedOut}

Experience = re.findall(r"Str\w+[\s]\w+[\s-]+[^\n]+", text_data)[0].split(" - ")
professionalExperience = {
        "from": Experience[2],
        "to":  Experience[3].strip(),
        "company_name": Experience[1].strip(),
        "position": Experience[0] 
    }
# print(professional_experience)

data_extracted = {"name": name.strip(), "address": address, "email":email, "phoneNumber": phoneNumber, "education" : education, "skills": skills, "experience": professionalExperience}


with open('resume_data.txt', 'w') as convert_file:
     convert_file.write(json.dumps(data_extracted))

print(json.dumps(data_extracted))

# print("data_extracted")

sys.stdout.flush()