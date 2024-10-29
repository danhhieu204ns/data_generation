from utils import func
import os

# thong ke so luong file cua moi nganh

db_path = "database"
output_path = "analize"
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"Thư mục {output_path} đã được tạo.")

func.count_file(db_path, output_path)

db_path = "freshdata"
output_path = "freshdata"
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"Thư mục {output_path} đã được tạo.")

func.count_file(db_path, output_path)


#kiem tra lai noisy_data
# db_path = "noisy_data/data"
# output_path = "check"
# if not os.path.exists(output_path):
#     os.makedirs(output_path)
#     print(f"Thư mục {output_path} đã được tạo.")

# func.count_file(db_path, output_path)
