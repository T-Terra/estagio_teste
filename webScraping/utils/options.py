from selenium.webdriver.chrome.options import Options


class ConfigOptions:
    def __init__(self, path_download_folder):
        self.path_download_folder = path_download_folder

    def make_options(self) -> Options:
        try:

            chrome_options = Options()

            chrome_options.add_experimental_option(
                "prefs",
                {
                    "download.default_directory": self.path_download_folder,
                    "download.prompt_for_download": False,
                    "download.directory_upgrade": True,
                    "plugins.always_open_pdf_externally": True,
                },
            )

            return chrome_options
        except Exception:
            print("Error: Options não foram adicionadas")
