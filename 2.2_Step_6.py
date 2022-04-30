from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.ID, 'input_value')
    x1 = x_element1.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x1)

    print(y)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option4 = browser.find_element(By.ID, "robotCheckbox")
    option4.click()

    option4 = browser.find_element(By.ID, "robotsRule")
    option4.click()

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла