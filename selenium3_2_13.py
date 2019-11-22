from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".first_block .first_class input")
        input1.send_keys("Имя")
        input2 = browser.find_element_by_css_selector(".first_block .second_class input")
        input2.send_keys("Фамилия")
        input3 = browser.find_element_by_css_selector(".first_block .third_class input")
        input3.send_keys("E-mail")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error in registration")
        browser.quit()

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".first_block .first_class input")
        input1.send_keys("Имя")
        input2 = browser.find_element_by_css_selector(".first_block .second_class input")
        input2.send_keys("Фамилия")
        input3 = browser.find_element_by_css_selector(".first_block .third_class input")
        input3.send_keys("E-mail")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error in registration")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
