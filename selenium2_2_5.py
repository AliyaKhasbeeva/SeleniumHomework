#Давайте теперь рассмотрим реальную ситуацию, когда пользователь должен кликнуть на элемент,
#который внезапно оказывается перекрыт другим элементом на странице.
#В итоге, чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды в коде:

from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
