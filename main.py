import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def login_to_site(driver, url, username, password):
    driver.get(url)
    
    time.sleep(2)

    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.TAG_NAME, 'button')

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()

    time.sleep(3) 

def run_automation():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    login_url = 'file:/Seu/Caminho/login.html'
    
    login_to_site(driver, login_url, 'seu_usuario', 'sua_senha') 
    
    print("Pressione Enter para fechar o navegador...")
    while True:
        if input() == '':
            break

    driver.quit()

if __name__ == "__main__":
    run_automation()
