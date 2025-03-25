from os import getcwd, path, makedirs, listdir, remove
from zipfile import ZipFile


class FileManager:
    def make_zip(self, path_download, list_pdf):
        try:
            zip_path = (
                f"{path_download}\\files.zip"  # Caminho para salvar o arquivo zip
            )

            with ZipFile(zip_path, "w") as zip_file:
                for file_name in list_pdf:
                    if file_name.endswith(".pdf"):
                        file_path = path.join(path_download, file_name)
                        zip_file.write(file_path, path.basename(file_path))
        except AttributeError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")

    def remove_files(self, path_download, list_pdf):
        try:
            for file in list_pdf:
                if file.endswith("pdf"):
                    file_path = path.join(path_download, file)

                    remove(file_path)
        except AttributeError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")

    """Funções auxiliares"""

    def make_folder(self, folder_path):
        try:
            if not path.isdir(folder_path):
                makedirs(folder_path, exist_ok=True)
        except AttributeError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")

    def List_dir(self, path_download) -> list[str]:
        try:
            files_pdf_path = listdir(path_download)  # Listagem do diretório downloads
            return files_pdf_path
        except AttributeError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")

    def get_folder_download(self):
        try:
            download_folder = f"{getcwd()}\\downloads\\"
            self.make_folder(download_folder)
            return download_folder
        except AttributeError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")
