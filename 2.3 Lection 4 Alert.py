from selenium import webdriver
import math


def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

option1 = browser.find_element_by_css_selector("[type='submit']")
option1.click()

confirm = browser.switch_to.alert
confirm.accept()


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
pole = browser.find_element_by_id("answer")
pole.send_keys(y)

option1 = browser.find_element_by_css_selector("[type='submit']")
option1.click()