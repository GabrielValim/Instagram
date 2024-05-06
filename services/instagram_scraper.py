#Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from django.shortcuts import redirect, reverse
from selenium.common.exceptions import TimeoutException


#Other imports
import os 
import re
from selenium.webdriver.common.keys import Keys
import time

def scrape_instagram_data(username, password):
    # A classe Service é usada para iniciar uma instancia do chrome webdriver
    service = Service()

    # Webdriver.ChromeOptions é usado para definir a preferencia para o browser chrome
    options = webdriver.ChromeOptions()

    # Inicia-se a instancia do Chrome WebDriver com as 'options' e 'service'
    driver = webdriver.Chrome(service=service, options=options)

    # Navegando até o Instagram
    link = "https://www.instagram.com/"
    driver.get(link)

    # Preenche o login e senha
    username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username_field.send_keys(username)
    password_field.send_keys(password)
    log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    # perdir a senha de segurança de 2 fatores
    redirect_to_security_page(driver) 
  

    # agora não 
    agora_Nao = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Agora não')]"))).click()
    agora_Nao2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Agora não')]"))).click()



    data_collected = {
        'followers': 1000,
        'following': 500,
        'posts': 200
    }

    # Fecha o navegador
    driver.quit()

    # Retorna os dados coletados
    return data_collected

def redirect_to_security_page(driver):
    try:
        # Aguardar até que a URL da página mude, indicando que o redirecionamento ocorreu
        WebDriverWait(driver, 30).until(lambda driver: 'seguranca' in driver.current_url)
        redirect('seguranca')
        
        # Redirecionar para a página de segurança
    except TimeoutException:
        # Houve um timeout ao aguardar o redirecionamento
        print("Não foi possível redirecionar para a página de segurança.")
        
        # Continuar com a coleta de dados
        return None
    except Exception as e:
        # Tratar outras exceções
        print(f"Ocorreu um erro: {e}")
        return None