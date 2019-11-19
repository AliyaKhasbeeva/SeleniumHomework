#Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду
# browser.find_element_by_id("button") после открытия страницы

from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")

    button1 = browser.find_element_by_id("button")
    button1.click()

finally:
    browser.quit()
