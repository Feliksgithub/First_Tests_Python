from selenium import webdriver
import time 
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    

    abc = browser.find_element_by_id("answer")
    abc.send_keys(y)
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    
    submit = browser.find_element_by_xpath("/html/body/div/form/button")
    submit.click()
    

    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    browser.quit()

   
