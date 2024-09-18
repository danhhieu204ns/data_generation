import os
import csv
import read_pdf

# thong ke so luong dong trung binh cua tung nganh

db_names = ["Accountant", "IT", "Japanese", "Luật", "QTKD"]
data_path = "analize/quantity_sent"


data = []

analize_path = "analize"
outfile_path = os.path.join(analize_path, "sent_average.csv")


for db_name in db_names:
    data_file =  os.path.join(data_path, f"{db_name}.csv")
    sum_line = 0
    sum_file = 0
    with open(data_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            sum_file += 1
            sum_line += int(row["Số lượng câu"])
    
    data.append({
        "Ngành học" : db_name,
        "Số lượng câu trung bình" : sum_line //sum_file
    })

fieldnames = data[0].keys()

with open(outfile_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
