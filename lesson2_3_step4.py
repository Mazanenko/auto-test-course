from selenium import webdriver
import time
import math

from selenium import webdriver

try:
    # Открываем страницу в браузере
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Жмем на кнопку
    button1 = browser.find_element_by_css_selector(".btn-primary")
    button1.click()

    # Accept Confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # Решаем капчу
    # Уравнение
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Считываем х
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    print(x)

    # Находим y
    y = calc(x)

    # Находим поле для ввода, вставляем значение y
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    # Жмём submit
    option1 = browser.find_element_by_css_selector(".btn-primary")
    option1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
