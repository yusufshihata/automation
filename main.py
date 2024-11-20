from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import random
import string


ua = UserAgent()
options = webdriver.FirefoxOptions()
options.add_argument(f'user-agent={ua.random}')
driver = webdriver.Firefox(options=options)

first_name = "marchal"
last_name = "mothers"
password = "jkdjfasdfasfdsf"


driver.get("https://accounts.google.com/signup")

wait = WebDriverWait(driver, 10)

def addUsername():
    try:
        wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first_name)
        driver.find_element(By.ID, "lastName").send_keys(last_name)

        driver.find_element(By.XPATH, "//span[text()='Next']").click()
    except:
        addUsername()

def setBirth():
    try:

        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='day']")))

        driver.find_element(By.XPATH, "//input[@id='day']").send_keys("15")  # Day selection (example)
        driver.find_element(By.XPATH, "//select[@id='month']").send_keys("January")  # Month selection (example)
        driver.find_element(By.XPATH, "//input[@id='year']").send_keys("1990")
        driver.find_element(By.XPATH, "//select[@id='gender']").send_keys("Male")

        driver.find_element(By.XPATH, "//span[text()='Next']").click()
    except:
        setBirth()

def setEmail():
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='selectionc2']")))

        button = driver.find_element(By.XPATH, "//div[@class='SCWude']")

        driver.execute_script("arguments[0].click();", button)

        gmail = driver.find_element(By.XPATH, "//div[@id='selectionc2']").text

        driver.find_element(By.XPATH, "//span[text()='Next']").click()


    except:
        setEmail()

    return gmail

def setPassword():
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='VfPpkd-vQzf8d']")))
        passwordForms = driver.find_elements(By.XPATH, "//input[@class='whsOnd zHQkBf']")

        for passwordForm in passwordForms:
            passwordForm.send_keys(password)

        driver.find_element(By.XPATH, "//span[text()='Next']").click()

    except:
        setPassword()

def main():

    addUsername()
    setBirth()
    email = setEmail()
    setPassword()

    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
    print(f"Email: {email}")
    print(f"password: {password}")

main()


