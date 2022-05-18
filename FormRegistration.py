from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys("Feliks")
    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Avetis")
    input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    input3.send_keys("12345@yandex.ru")
    input4 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[1]/input')
    input4.send_keys("+7 933 5632545")
    input5 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/input')
    input5.send_keys('Kashtanovaya street 45')
    
    time.sleep(3)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()