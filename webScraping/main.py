from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


from utils.options import ConfigOptions
from utils.file_manager import FileManager


def main():
    # Configurações
    file_manager = FileManager()

    chrome_options = ConfigOptions(file_manager.get_folder_download()).make_options()

    # acessa o site
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    sleep(2)

    driver.get(
        "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    )

    sleep(2)
    # faz o download dos arquivos

    driver.find_element(By.XPATH, "//body").click()

    sleep(1)

    """Baixa o arquivo Anexo I"""
    driver.find_element(
        By.XPATH, '//a[contains(@href, ".pdf") and contains(text(), "Anexo I.")]'
    ).click()

    sleep(10)

    driver.find_element(
        By.XPATH, '//a[contains(@href, ".pdf") and contains(text(), "Anexo II.")]'
    ).click()

    sleep(5)

    driver.quit()

    # Campactação de arquivos pdf

    dir_download_path = file_manager.get_folder_download() # pega o caminho do diretório download
    list_pdf_str= file_manager.List_dir(dir_download_path) # lista dos arquivos pdf


    file_manager.make_zip(dir_download_path, list_pdf_str)

    file_manager.remove_files(dir_download_path, list_pdf_str)


if __name__ == "__main__":
    main()
