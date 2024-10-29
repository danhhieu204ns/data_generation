from utils import func
import os

# thong ke so luong dong cua moi file thuoc tung nganh

db_path = "database"
output_path = "analize/quantity_sent"
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"Thư mục {output_path} đã được tạo.")

func.count_sentence(db_path, output_path)


db_path = "freshdata"
output_path = "freshdata/quantity_sent"
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"Thư mục {output_path} đã được tạo.")

func.count_sentence(db_path, output_path)


#kiem tra lai noisy_data
# db_path = "noisy_data/data"
# output_path = "check/quantity_sent"
# if not os.path.exists(output_path):
#     os.makedirs(output_path)
#     print(f"Thư mục {output_path} đã được tạo.")

# func.count_sentence(db_path, output_path)