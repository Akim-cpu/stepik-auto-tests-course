# from selenium import webdriver
# import os
# import time
#
#
# try:
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element_by_name("firstname").send_keys("sdhfs")
#     browser.find_element_by_name("lastname").send_keys("sdhfs")
#     browser.find_element_by_name("email").send_keys("sdhfs")
#
#
#
#
#     # получаем путь к директории текущего исполняемого скрипта lesson2_7.py          |
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#
#     # имя файла, который будем загружать на сайт                                     |
#     file_name = "file_example.txt"
#
#     # получаем путь к file_example.txt                                               |
#     file_path = os.path.join(current_dir, file_name)
#
#     browser.find_element_by_name("file").send_keys(file_path)
#     browser.find_element_by_class_name("btn").click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# !!! NEW CODE !!!

# from selenium import webdriver
# import time
# from math import sin, log
#
# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element_by_class_name("btn").click()
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     value = browser.find_element_by_id("input_value")
#     value_txt = value.text
#     x = value_txt
#
#
#     def calc(x):
#         return (log(abs(12*sin(int(x)))))
#
#
#     y = calc(x)
#     browser.find_element_by_id("answer").send_keys(str(y))
#     browser.find_element_by_class_name("btn").click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# import time
# from math import sin, log
#
# try:
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     time.sleep(5)
#     browser.find_element_by_class_name("trollface").click()
#
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#     # confirm = browser.switch_to.alert
#     # confirm.accept()
#
#     value = browser.find_element_by_id("input_value")
#     value_txt = value.text
#     x = value_txt
#
#
#     def calc(x):
#         return (log(abs(12*sin(int(x)))))
#
#
#     y = calc(x)
#     browser.find_element_by_id("answer").send_keys(str(y))
#     browser.find_element_by_class_name("btn").click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
#
# browser.implicitly_wait(5)
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text


# from selenium import webdriver
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text


from selenium import webdriver
import time
from math import log, sin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), str(100))
    )
    browser.find_element_by_id("book").click()

    value = browser.find_element_by_id("input_value")
    value_txt = value.text
    x = value_txt


    def calc(x):
         return (log(abs(12*sin(int(x)))))


    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id("answer").send_keys(str(y))

    browser.find_element_by_id("solve").click()

finally:
    time.sleep(5)
    browser.quit()
    
    
#валерарулидд
