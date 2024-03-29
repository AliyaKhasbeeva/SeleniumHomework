#Открыть страницу http://suninjuly.github.io/alert_accept.html
#Нажать на кнопку
#принять confirm
#На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
