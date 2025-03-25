from utils.file_manager import FileManager
from utils.abstract_driver import ChromeDriver


def main():
    # Configurações
    file_manager = FileManager()
    chrome = ChromeDriver()

    # acessa o site

    chrome.start_browser()

    chrome.browsing_to(2)

    chrome.click_element("//body", 2)

    # """Baixa o arquivo Anexo I"""

    chrome.click_element('//a[contains(@href, ".pdf") and contains(text(), "Anexo I.")]', 10)

    chrome.click_element('//a[contains(@href, ".pdf") and contains(text(), "Anexo II.")]', 10)

    chrome.close_browser()

    # Campactação de arquivos pdf

    dir_download_path = (
        file_manager.get_folder_download()
    )  # pega o caminho do diretório download
    list_pdf_str = file_manager.List_dir(dir_download_path)  # lista dos arquivos pdf

    file_manager.make_zip(dir_download_path, list_pdf_str, 2)

    file_manager.remove_files(dir_download_path, list_pdf_str)


if __name__ == "__main__":
    main()
