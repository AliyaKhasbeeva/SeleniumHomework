#Добавьте в самый верх своего кода import math
#Добавьте команду в код, которая откроет страницу: http://suninjuly.github.io/find_link_text
#Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
#str(math.ceil(math.pow(math.pi, math.e)*10000))
#Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
#Заполните скриптом форму так же как вы делали в предыдущем шаге урока
#После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание

from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link = browser.find_element_by_link_text(x)
    link.click()

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
    time.sleep(10)
    browser.quit()
