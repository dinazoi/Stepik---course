from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

First_name = browser.find_element_by_xpath("//*[@placeholder='Enter first name']")
First_name.send_keys("Oleg")

Last_name = browser.find_element_by_xpath("//*[@placeholder='Enter last name']")
Last_name.send_keys("Testovich")

Email_name = browser.find_element_by_xpath("//*[@placeholder='Enter email']")
Email_name.send_keys("Test@email.com")


current_dir = os.path.abspath(os.path.dirname("C:/Users/Unknow/PycharmProjects/Pybot_lesson/Section_2/"))
file_path = os.path.join(current_dir, 'test.txt')
file_exe = browser.find_element_by_id('file')
#file_exe.click()
file_exe.send_keys(file_path)

option3 = browser.find_element_by_css_selector("[type='submit']")
option3.click()

