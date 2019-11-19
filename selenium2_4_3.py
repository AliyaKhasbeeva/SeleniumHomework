#Открыть страницу http://suninjuly.github.io/wait1.html
#Нажать на кнопку "Verify"
#Проверить, что появилась надпись "Verification was successful!"

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    time.sleep(3) #т.к.на странице кнопка появляется позже
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    time.sleep(10)
    browser.quit()