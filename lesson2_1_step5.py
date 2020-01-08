from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение X
    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute
    y = calc(x)

    # Ввести ответ в текстовое поле
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    #Отметить checkbox
    option1 = browser.find_element_by_css_selector('#robotCheckbox')
    option1.click()

    #Выбрать radiobutton
    option2 = browser.find_element_by_css_selector('#robotsRule')
    option2.click()

    #Нажать submit
    option3 = browser.find_element_by_css_selector('.btn-default')
    option3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
