from selenium import webdriver
import math


def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)




x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
#x = x_element.text
y = calc(x)
print(x)
pole = browser.find_element_by_id("answer")
pole.send_keys(y)


option1 = browser.find_element_by_id("robotCheckbox")
option1.click()
option2 = browser.find_element_by_id("robotsRule")
option2.click()
option3 = browser.find_element_by_css_selector("[type='submit']")
option3.click()