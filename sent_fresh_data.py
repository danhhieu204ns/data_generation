import os
import csv
import read_pdf

# thong ke so luong dong cua moi file thuoc tung nganh

db_names = ["Accountant", "IT", "Japanese", "Luật", "QTKD"]
db_path = "freshdata"


for db_name in db_names:
    data = []
    folder_path = os.path.join(db_path, db_name)

    analize_path = "freshdata/quantity_sent"
    outfile_path = os.path.join(analize_path, f"{db_name}.csv")

    pdf_files = [f for f in os.listdir(folder_path)]

    for file in pdf_files:
        file_path = os.path.join(folder_path, file)
        pdf_text = read_pdf.read_pdf(file_path)
        
        sentences = read_pdf.split_into_sentences(pdf_text)
        data.append({
            "File name" : file,
            "Số lượng câu" : len(sentences)
        })

    fieldnames = data[0].keys()

    with open(outfile_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
