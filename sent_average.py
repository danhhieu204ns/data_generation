import os
import csv
from utils import func

# thong ke so luong dong trung binh cua tung nganh

# data_path = "analize/quantity_sent"
# output_path = "analize"

data_path = "freshdata/quantity_sent"
output_path = "freshdata"

func.cal_average_sententce(data_path, output_path)