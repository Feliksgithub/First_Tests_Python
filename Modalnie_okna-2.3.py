from selenium import webdriver
import time 
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#Присваиваем link = ссылку
link = "http://suninjuly.github.io/alert_accept.html"

try:
    #Присваиваем переменной browser = открытие вебдрайвера хром
    browser = webdriver.Chrome()
    #Открываем ссылку присвоенную link выше
    browser.get(link)
    #Находим и нажимаем кнопку
    browser.find_element_by_xpath("/html/body/form/div/div/button").click()

    time.sleep(2)
    #присваиваем алерту метод алерт
    alert = browser.switch_to.alert
    #принимаем модальное окно
    alert.accept()

    #Находим элемент с числом (пока это текстовое значение для питона)
    x_element = browser.find_element_by_id("input_value")
    #Извлекаем число(как текст)из элемента
    x = x_element.text
    #Высчитываем формулу (в начале скрипта она поисана)
    y = calc(x)
    #Находим, заполняем и отправляем поле для ответа
    abc = browser.find_element_by_id("answer")
    abc.send_keys(y)
    #Находим и нажимаем кнопку  submit
    submit = browser.find_element_by_xpath('/html/body/form/div/div/button')
    submit.click()
    

    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    browser.quit()
