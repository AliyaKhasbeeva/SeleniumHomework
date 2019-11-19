#В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о
# пользователях своего продукта. В награду за заполнение формы становится доступен код на скидку.
# Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей и ограничив
# время на ее заполнение. Теперь эта задача под силу только роботам

#в цикле for мы можем последовательно взять каждый элемент из найденного списка
# текстовых полей и отправить произвольный текст в каждое поле.

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("Murrr")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
