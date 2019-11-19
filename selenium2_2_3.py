#Открыть страницу http://suninjuly.github.io/selects1.html
#Посчитать сумму заданных чисел
#Выбрать в выпадающем списке значение равное расчитанной сумме
#Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    z = int(x) + int(y)
    z1 = str(z)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(z1)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
