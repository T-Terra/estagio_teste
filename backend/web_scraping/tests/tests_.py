from os import getcwd, path, makedirs, listdir, remove
from utils.file_manager import FileManager

def test_make_dir_download():
    file_manager = FileManager()

    path_dir_download = file_manager.get_folder_download()

    file_manager.make_folder(path_dir_download)

    assert path.isdir(path_dir_download) == True

def test_make_file_zip():
    file_manager = FileManager()

    path_dir_download = file_manager.get_folder_download()
    list_pdf_str = file_manager.List_dir(path_dir_download)

    file_manager.make_zip(path_dir_download, list_pdf_str)

    check_zip = file_manager.List_dir(path_dir_download)

    assert check_zip == ['files.zip']

def test_remove_files():
    file_manager = FileManager()
    dir_download_path = file_manager.get_folder_download()
    list_pdf_str = file_manager.List_dir(dir_download_path)

    file_manager.remove_files(dir_download_path, list_pdf_str)

    assert list_pdf_str == ['files.zip'] or []

def test_list_dir_files():
    file_manager = FileManager()
    dir_download_path = file_manager.get_folder_download()

    list_pdf_str = file_manager.List_dir(dir_download_path)

    assert list_pdf_str == ['files.zip'] or []

def test_get_folder_path():
    file_manager = FileManager()

    path_dir_download = file_manager.get_folder_download()

    assert path_dir_download == f"{getcwd()}\\downloads\\"
