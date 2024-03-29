# Проверьте, что можно зарегистрироваться на сайте,
# заполнив только обязательные поля, отмеченные символом *:
# First name, last name, email. Текст для полей может быть любым.
# Успешность регистрации проверяется сравнением ожидаемого текста
# "Congratulations! You have successfully registered!" с текстом на странице,
# которая открывается после регистрации. Для сравнения воспользуемся
# стандартной конструкцией assert из языка Python.

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".first_block .first_class input")
    input1.send_keys("Имя")
    input2 = browser.find_element_by_css_selector(".first_block .second_class input")
    input2.send_keys("Фамилия")
    input3 = browser.find_element_by_css_selector(".first_block .third_class input")
    input3.send_keys("E-mail")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
