import tabula
import PyPDF2
from os import getcwd, path, listdir
from zipfile import ZipFile

def main(pdf_path, output_csv_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)
        
    pages = 3

    while True:
        if pages > total_pages:
            break

        doc = tabula.read_pdf(pdf_path, pages=pages, lattice=True)
        if len(doc) == 1:
            if pages == 3:
                table = doc[0]
                table.to_csv(output_csv_path, mode="a", index=False)
                pages += 1
            else:
                table = doc[0]
                table.to_csv(output_csv_path, mode="a", index=False, header=False)
                pages += 1
        elif len(doc) > 1:
            print(len(doc), f"page: {pages}")
        else:
            break
    

def make_zip(path_download, list_files):
    zip_path = (
        f"{path_download}\\Teste_gabriel_terra.zip" 
    )

    with ZipFile(zip_path, "w") as zip_file:
        for file_name in list_files:
            if file_name.endswith(".csv"):
                file_path = path.join(path_download, file_name)
                zip_file.write(file_path, path.basename(file_path))

pdf_path = f"{getcwd()}\\downloads\\files\\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_output_path = f"{getcwd()}\\downloads\\data_table.csv"
path_download = f"{getcwd()}\\downloads\\"
files_list = listdir(path_download)

if __name__ == '__main__':
    main(pdf_path, csv_output_path, path_download, files_list)
    make_zip(path_download, files_list)