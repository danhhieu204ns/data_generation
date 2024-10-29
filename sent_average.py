from utils import func

# # thong ke so luong dong trung binh cua tung nganh

data_path = "analize/quantity_sent"
output_path = "analize"

func.cal_average_sententce(data_path, output_path)

#Khong can tinh toan so luong cau trung binh doi voi fresh data
data_path = "freshdata/quantity_sent"
output_path = "freshdata"

func.cal_average_sententce(data_path, output_path)


#kiem tra lai noisy_data
# data_path = "check/quantity_sent"
# output_path = "check"

# func.cal_average_sententce(data_path, output_path)