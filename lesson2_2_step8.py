
import time

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Заполняем поле first name
    option1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    option1.send_keys ("Ivan")

    #Заполняем поле last name
    option2 = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    option2.send_keys("Ivanov")

    # Заполняем поле Email
    option3 = browser.find_element_by_css_selector('[name="email"]')
    option3.send_keys('mail@mail.com')
    
    # Загружаем текстовый файл
    import os 

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt') 

    option4 = browser.find_element_by_css_selector('#file')
    option4.send_keys(file_path)
    
     # Нажать submit
    option5 = browser.find_element_by_css_selector(".btn-primary")
    option5.click()
    
    
finally:
    time.sleep(10)
    browser.quit()
