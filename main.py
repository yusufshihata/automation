from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

first_name = "marchal"
last_name = "mothers"
password = "jkdjfasdfasfdsf"


driver = webdriver.Firefox()

def main():
    driver.get("https://accounts.google.com/signup")

    wait = WebDriverWait(driver, 80)

    try:
# Wait for the page to load and locate form fields
        wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first_name)
        driver.find_element(By.ID, "lastName").send_keys(last_name)

# Submit the form (you may need to handle additional steps like CAPTCHA manually)
        driver.find_element(By.XPATH, "//span[text()='Next']").click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='day']")))

# Select birthdate (day, month, year)
        driver.find_element(By.XPATH, "//input[@id='day']").send_keys("15")  # Day selection (example)
        driver.find_element(By.XPATH, "//select[@id='month']").send_keys("January")  # Month selection (example)
        driver.find_element(By.XPATH, "//input[@id='year']").send_keys("1990")
        driver.find_element(By.XPATH, "//select[@id='gender']").send_keys("Male")

        driver.find_element(By.XPATH, "//span[text()='Next']").click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='selectionc2']")))

        button = driver.find_element(By.XPATH, "//div[@class='SCWude']")

        driver.execute_script("arguments[0].click();", button)

        gmail = driver.find_element(By.XPATH, "//div[@id='selectionc2']").text

        driver.find_element(By.XPATH, "//span[text()='Next']").click()

    
        print(f"First name: {first_name}")
        print(f"Last name: {last_name}")
        print(f"Email: {gmail}")
        print(f"password: {password}")

    except:
        main()

    passwords = driver.find_elements(By.XPATH, "//input[@class='whsOnd zHQkBf']")

    for i in passwords:
        i.send_keys(password)

main()


