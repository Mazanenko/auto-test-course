from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
try:
    # переходим по ссылке
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # ждём снижения цены до 100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
         )

    # жмём кнопку 'Book'
    button = browser.find_element_by_css_selector("#book")
    button.click()

    # Уравнение
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Считываем х
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text

    # Находим y
    y = calc(x)

    # Находим поле для ввода, вставляем значение y
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    # Жмём submit
    option1 = browser.find_element_by_css_selector("#solve")
    option1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
