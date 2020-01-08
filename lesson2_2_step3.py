from selenium import webdriver
import time
import math




try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение X
    x_element = browser.find_element_by_css_selector('#num1')
    x = x_element.text

    # Находим значение X
    y_element = browser.find_element_by_css_selector('#num2')
    y = y_element.text

    # Находим сумму X и Y
    def summ(x,y):
        return str(int(x) + int(y))


    # Выбираем значение из списка
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(summ(x,y))

    # Нажать submit
    option3 = browser.find_element_by_css_selector('.btn-default')
    option3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
