#Вам нужно открыть страницу по ссылке и заполнить форму
#на этой странице с помощью Selenium. Если всё сделано
#правильно, то вы увидите окно с проверочным кодом. Это
#число вам нужно ввести в качестве ответа в этой задаче

from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"

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
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
