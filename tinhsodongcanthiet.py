import csv, os

db_names = ["Accountant", "IT", "Japanese", "Luật", "QTKD"]
noisy = 0.9


def get_average(data_file):
    data = []
    with open(data_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row["Số lượng câu trung bình"])
    return data

def tinh_so_dong(average_file, outfile_path):
    db_data = get_average(average_file)
    data = []
    for i in range(5):
        data.append({
            "Ngành học" : db_names[i],
            "Số lượng câu láy từ freshdata" : int(int(db_data[i]) * (1 - noisy)) +1,
            "Số lượng câu lấy từ DB" : int(int(db_data[i]) * noisy) +1
        })

    fieldnames = data[0].keys()
    with open(outfile_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

average_file = "analize/sent_average.csv"
outfile_path = "num_sent_required.csv"

tinh_so_dong(average_file, outfile_path)