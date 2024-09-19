from utils import func

# thong ke so luong dong cua moi file thuoc tung nganh

# db_path = "database"
# output_path = "analize/quantity_sent"

db_path = "freshdata"
output_path = "freshdata/quantity_sent"


func.count_sentence(db_path, output_path)