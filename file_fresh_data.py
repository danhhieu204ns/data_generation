import os
import csv

# thong ke so luong file cua moi nganh trong fresh data

db_names = ["Accountant", "IT", "Japanese", "Luật", "QTKD"]
db_path = "freshdata"

data = []

for db_name in db_names:
    folder_path = os.path.join(db_path, db_name)
    pdf_files = [f for f in os.listdir(folder_path)]
    data.append({
        "Ngành học": db_name, 
        "Số lượng file": len(pdf_files)
    })

analize_path = "freshdata"
outfile_path = os.path.join(analize_path, f"quantity_pdf.csv")

fieldnames = data[0].keys()

with open(outfile_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)