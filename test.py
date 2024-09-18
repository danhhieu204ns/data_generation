import read_pdf
import os


# db_names = ["Accountant", "IT", "Japanese", "Luật", "QTKD"]
db_names = ["IT"]
db_path = "database"

for db_name in db_names:
    folder_path = os.path.join(db_path, db_name)

    pdf_files = [f for f in os.listdir(folder_path)]
    analize_path = "test"
    outfile_path = os.path.join(analize_path, f"{db_name}.txt")
    with open(outfile_path, "w", encoding="utf-8") as outfile:
        outfile.write(str(f"Số lượng file PDF: {len(pdf_files)}"))
        outfile.write("\n\n\n")

        for file in pdf_files:
            file_path = os.path.join(folder_path, file)
            pdf_text = read_pdf.read_pdf(file_path)
            
            outfile.write(f"File: {file}")
            outfile.write("\n")
            sentences = read_pdf.split_into_sentences(pdf_text)
            for s in sentences:
                outfile.write(s)
                outfile.write("\n")
            outfile.write(str(len(sentences)))
            outfile.write("\n")

            break

        
        outfile.write("\n")