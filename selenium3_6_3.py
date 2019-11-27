# окрыть страницу
# ввести правильный ответ
# нажать кнопку "Отправить"
# дождаться фидбека о том, что ответ правильный
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898",
                                   "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, links):
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    answer = str(math.log(int(time.time())))
    input1 = browser.find_element_by_css_selector(".textarea")
    input1.send_keys(answer)
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    text11 = browser.find_element_by_css_selector(".smart-hints__hint")
    text1 = text11.text
    assert "Correct!" == text1, 'Text for my answer: {}'.format(text1)
