#В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
#Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit.
# XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
#Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
#Запустите ваш код.

from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//button[@type = "submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()