from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def browser(): 

    # A classe Service é usada para iniciar uma instancia do chrome webdriver
    service = Service()

    # Webdriver.ChromeOptions é usado para definir a preferencia para o browser chrome
    options = webdriver.ChromeOptions()

    # Inicia-se a instancia do Chrome WebDriver com as 'options' e 'service'
    driver = webdriver.Chrome(service=service, options=options)

    # Navegando até o Instagram
    link = "https://www.instagram.com/"
    driver.get(link)
