from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_name = "test.txt"
    print(file_name)
    file_path = os.path.join(current_dir, file_name)
    print(file_path)
    #with open("test.txt", "w") as file:
        #content = file.write("automationbypython")  # create test.txt file

    elements = browser.find_elements(By.CSS_SELECTOR, ".form-control")
    for element in elements:
        element.send_keys("Мойответ")

    option3 = browser.find_element(By.ID, "file")
    option3.send_keys(file_path)

    option4 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    option4.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла