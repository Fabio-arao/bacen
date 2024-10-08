from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from abc import ABC
import os


class PageElement(ABC): 
    """
    Classe abstrata onde contém 
    todos os elementos, métodos e funções necessários para
    iteragir com webelements.
    """      
    def __init__(self, webdriver):
        """
        Método construtor para iniciar o webdriver

        Args:
            webdriver: webdriver que será executado
            url (str, optional): url para acesso à adm. Defaults to ''.
        """
        self.webdriver = webdriver
        self.webdriver.maximize_window()
    
    def wait_(self, t=60):
        return WebDriverWait(self.webdriver, t)
      
    def find(self, locator):
        """
        Encontra o WebElement de acordo com seu locator

        Args:
            locator (tuple): tupla com as informações do WebElement

        Returns:
            WebElement: Elemento do DOM
        """
        return self.webdriver.find_element(*locator)
    
    def finds(self, locator):
        """
        Encontra os WebElements de acordo com seu locator

        Args:
            locator (tuple): tupla com as informações do WebElement

        Returns:
            WebElement (list): lista com os elementos encontrados.
        """
        return self.webdriver.find_elements(*locator)  
        
    def open_url(self, url):
        """
        Abre a url mo navegador
        """
        self.webdriver.get(url)

    def switch_to_frame(self, to):
        """
        Muda para o frame passado por parâmetro (to)

        Args:
            to (string): nome do frame que quer alterar
        """
        return self.webdriver.switch_to.frame(to)

class ConfigWebDriver():
    def __init__(self):
        self.s=Service(ChromeDriverManager(version="114.0.5735.90").install())
        self.options = ChromeOptions()
        self.prefs = {"download.default_directory" : os.getcwd(),         
                      "profile.content_settings.exceptions.automatic_downloads.*.setting": 1 }
        self.options.add_experimental_option("prefs", {"focus_on_tab_change": False})
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_experimental_option("prefs", self.prefs) 