from selenium import webdriver
import time 
import math
def calc(x, y):
    return str(int(x)+int(y))
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    z = calc(x, y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)

    #browser.find_element_by_tag_name("select").click()
    #browser.find_element_by_css_selector("[value='1']").click()
    
    

    #abc = browser.find_element_by_id("answer")
    #abc.send_keys(y)
    
    #option1 = browser.find_element_by_id("robotCheckbox")
    #option1.click()
    
    #radiobutton = browser.find_element_by_id("robotsRule")
    #radiobutton.click()
    time.sleep(1)
    
    submit = browser.find_element_by_xpath("/html/body/div/form/button")
    submit.click()
    

    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    browser.quit()

   
