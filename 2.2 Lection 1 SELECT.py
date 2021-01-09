from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1")
x1 = int(num1.text)
num2 = browser.find_element_by_id("num2")
x2 = int(num2.text)
total_count = x1 + x2
print(total_count)

#option1 = browser.find_element_by_id("dropdown")
#option1.click()
#option2 = browser.find_element_by_css_selector("[value='total_count']")
#option2.click()



select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(total_count))
but = browser.find_element_by_css_selector("[type='submit']")
but.click()