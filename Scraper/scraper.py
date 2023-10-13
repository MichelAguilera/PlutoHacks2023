from selenium import webdriver
from rich.console import Console

url = "https://www.selenium.dev/selenium/web/web-form.html"

class Scraper:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def get_website(self):
        self.driver.get(url)

class Collector:
    def __init__(self) -> [str]:
        self.collection = []

    def add(self, item):
        self.collection.append(item)

    def repr(self):
        c = Console()
        c.print(self.collection)