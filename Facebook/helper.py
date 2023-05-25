

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def webdriver_browser(browser = "CHROME"):
    driver = None
    match browser.upper():
        case "CHROME":
            driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
        case "EDGE":
            driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    return driver