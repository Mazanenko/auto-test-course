import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение X
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    # Отметить checkbox
    option1 = browser.find_element_by_css_selector('#robotCheckbox')
    option1.click()

    # прокрутка страницы и выбор radiobutton
    option2 = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    # Нажать submit
    option3 = browser.find_element_by_css_selector(".btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option3)
    option3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
