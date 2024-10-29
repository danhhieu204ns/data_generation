import os, random, csv
from utils import func
from datetime import datetime
from fpdf import FPDF


db_names = ["Accountant", "IT", "Japanese", "Luật", "QTKD"]
names = ["Accountant", "IT", "Japanese", "Luật"]


def create_pdf(sentences, outfile):
    pdf = FPDF()
    pdf.add_font('Times', '', 'static\SVN_Times_New_Roman.ttf', uni=True)
    pdf.set_font('Times', '', 12)
    pdf.set_left_margin(25)   # Lề trái
    pdf.set_right_margin(25)  # Lề phải
    pdf.set_top_margin(25)    # Lề trên
    pdf.add_page()
    margin_bottom = 20  
    text = ' '.join(sentences)
    pdf.multi_cell(0, 10, text)
    if pdf.get_y() > pdf.h - margin_bottom:
        pdf.add_page()  
    pdf.output(outfile)
    print(f"PDF file created at: {outfile}")


def get_random_sentences(sentences, num):
    random_sentences = random.sample(sentences, num)
    return random_sentences

def get_fresh_sentences(sentences, db_cnt_max):
    
    return get_random_sentences(list(sentences), db_cnt_max)

def get_db_sentences(folder_path, sent_num, logfile_path):
    pdf_files = [f for f in os.listdir(folder_path)]
    data = []
    num_sent_in_file = sent_num // len(pdf_files) + 1

    with open(logfile_path, 'w', newline='', encoding='utf-8') as out_file:
        for file in pdf_files:
            file_path = os.path.join(folder_path, file)

            pdf_text = func.read_pdf(file_path)
            sentences = func.split_into_sentences(pdf_text)
            rand_sent = get_random_sentences(list(sentences), num_sent_in_file)
            data = data + rand_sent
            
            time = datetime.now()
            out_file.write("Created_at: ")
            out_file.write(str(time))
            out_file.write("\n")
            out_file.write("Src: ")
            out_file.write(file_path)
            out_file.write("\n")
            out_file.write("\n")
            for sent in rand_sent:
                out_file.write(sent)
                out_file.write("\n")
        
    return data

def get_max_num(data_file):
    db_cnt_max = []
    fresh_cnt_max = []
    with open(data_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            db_cnt_max.append(int(row["Số lượng câu lấy từ DB"]))
            fresh_cnt_max.append(int(row["Số lượng câu láy từ freshdata"]))

    return list(db_cnt_max), list(fresh_cnt_max)


db_data = "database"
fresh_data= "freshdata"
output = "noisy_data/data"
if not os.path.exists(output):
    os.makedirs(output)
    print(f"Thư mục {output} đã được tạo.")
log = "noisy_data/log"
if not os.path.exists(log):
    os.makedirs(log)
    print(f"Thư mục {log} đã được tạo.")

def merge_file():
    for i in range(5):
        if db_names[i] in names:
            continue
        fresh_path = os.path.join(fresh_data, db_names[i])
        db_path = os.path.join(db_data, db_names[i])
        output_path = os.path.join(output, db_names[i])
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"Thư mục {output_path} đã được tạo.")
        log_path = os.path.join(log, db_names[i])
        if not os.path.exists(log_path):
            os.makedirs(log_path)
            print(f"Thư mục {log_path} đã được tạo.")

        db_cnt_max, fresh_cnt_max = get_max_num("num_sent_required.csv")
        pdf_files = [f for f in os.listdir(fresh_path)]
        for file in pdf_files:
            file_path = os.path.join(fresh_path, file)
            pdf_text = func.read_pdf(file_path)
            sentences = func.split_into_sentences(pdf_text)
            outfile_path = os.path.join(output_path, f"{file}")
            logfile_path = os.path.join(log_path, f"log_{file}.txt")
            fresh_sent = get_fresh_sentences(list(sentences), fresh_cnt_max[i]) #get in fresh data
            db_sents = get_db_sentences(db_path, db_cnt_max[i], logfile_path) #get in db
            final_sent = fresh_sent + db_sents

            create_pdf(final_sent, outfile_path)
            
        print(f"\n\n Created successful {output_path}!\n\n")
        

merge_file()
