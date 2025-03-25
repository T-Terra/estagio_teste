import tabula
import PyPDF2
from os import getcwd

# Função para extrair texto do PDF e salvar em CSV
def main(pdf_path, output_csv_path):
    # Abrir o documento PDF

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
                print(pages)
                table = doc[0]
                table.to_csv(output_csv_path, mode="a", index=False)
                pages += 1
            else:
                print(pages)
                table = doc[0]
                table.to_csv(output_csv_path, mode="a", index=False, header=False)
                pages += 1
        elif len(doc) > 1:
            print(len(doc), f"page: {pages}")
            table = doc[0]
            table.to_csv("maior.csv", mode="a", index=False)
            pages += 1
        else:
            break


pdf_path = f"{getcwd()}\\downloads\\files\\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_output_path = "output_table.csv"

if __name__ == '__main__':
    # Chamar a função para extrair a tabela e salvar em CSV
    main(pdf_path, csv_output_path)