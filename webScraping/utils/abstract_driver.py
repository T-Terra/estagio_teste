from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.options import ConfigOptions
from utils.file_manager import FileManager
from dotenv import load_dotenv
from os import getenv
from time import sleep

load_dotenv(override=True)

class BaseDriver(ABC):
    def __init__(self):
        self.driver = None
    
    @abstractmethod
    def start_browser(self):
        pass

    @abstractmethod
    def close_browser(self):
        pass

class ChromeDriver(BaseDriver):
    def start_browser(self, wait: int = 1):
        try:
            file_manager = FileManager()
            service = self.get_service()

            chrome_options = ConfigOptions(file_manager.get_folder_download()).make_options()
            self.driver = webdriver.Chrome(service=service, options=chrome_options)

            sleep(wait)

            return self.driver
        except Exception as error:
            print(f"Error: {error}")
    
    def close_browser(self):
        if self.driver:
            self.driver.quit()
    
    def get_service(self) -> Service:
        try:
            service = Service(ChromeDriverManager().install())
            return service
        except Exception as error:
            print(f"Error: {error}")
    
    def browsing_to(self, wait: int = 1):
        try:
            sleep(wait)
            self.driver.get(
                getenv("URL")
            )
        except Exception as error:
            print(f"Error: {error}")
    
    def click_element(self, xpath: str, wait: int = 1):
        try:
            self.driver.find_element(By.XPATH, xpath).click()
            sleep(wait)
        except Exception as error:
            print(f"Error: {error}")

        