import pymupdf  # PyMuPDF
import csv
from os import getcwd
import re

# Função para extrair texto do PDF e salvar em CSV
def extract_table_from_pdf(pdf_path, output_csv_path):
    # Abrir o documento PDF
    doc = pymupdf.open(pdf_path)
    
    # Criar ou abrir o arquivo CSV para escrita
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        
        # Iterar pelas páginas do documento
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)  # Carregar a página
            text = page.get_text("text")  # Obter o texto da página
            
            # Regex para identificar linhas da tabela
            # Exemplo: captura de linhas com 3 colunas separadas por espaços ou tabulações
            # Ajuste a regex conforme a estrutura real do seu PDF
            pattern = r"(\S+)\s+(\S+)\s+(\S+)"  # Regex para capturar 3 colunas (modifique conforme necessário)
            matches = re.findall(pattern, text)
            
            # Escrever os dados extraídos no CSV
            for match in matches:
                writer.writerow(match)  # Escrever cada linha no arquivo CSV

# Caminho para o arquivo PDF e o arquivo CSV de saída
pdf_path = f"{getcwd()}\\downloads\\files\\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_output_path = "output_table.csv"

# Chamar a função para extrair a tabela e salvar em CSV
extract_table_from_pdf(pdf_path, csv_output_path)