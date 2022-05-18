from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath("/html/body/div/form/div/input[1]").send_keys("Feliks")

    lastname = browser.find_element_by_xpath('/html/body/div/form/div/input[2]')
    lastname.send_keys('Avetis')

    email = browser.find_element_by_xpath('/html/body/div/form/div/input[3]')
    email.send_keys('123@yandex.ru')

    #загрузка файла из той же директории что и скрипт
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "111.txt"
    file_path = os.path.join(current_dir, file_name)
    browser.find_element_by_xpath("//*[@id='file']").send_keys(file_path)


    submit = browser.find_element_by_xpath("/html/body/div/form/button")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
    #driver.quit()


