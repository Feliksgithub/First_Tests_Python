from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #драйвер ждет пока значение в строке с id=price будет 100, находит и нажимает кнопку book
    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_id("book")
    button.click()
    
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
 

    abc = browser.find_element_by_id("answer")
    abc.send_keys(y)
    
   
    submit = browser.find_element_by_id("solve")
    submit.click()

    alert = browser.switch_to.alert
    answer = alert.text.split()[1]
    print(answer)
    alert.accept()
    

    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    browser.quit()
