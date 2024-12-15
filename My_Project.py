from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    print("Navigating to the Parabank website...")
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    driver.implicitly_wait(10)

    print("Filling out the registration form...")
    driver.find_element(By.ID, "customer.firstName").send_keys("Kaspian")
    driver.find_element(By.ID, "customer.lastName").send_keys("Raihan")
    driver.find_element(By.ID, "customer.address.street").send_keys("123 savar, Dhaka")
    driver.find_element(By.ID, "customer.address.city").send_keys("Savar, Dhaka")
    driver.find_element(By.ID, "customer.address.state").send_keys("Bangladesh")
    driver.find_element(By.ID, "customer.address.zipCode").send_keys("1216")
    driver.find_element(By.ID, "customer.phoneNumber").send_keys("01745262631")
    driver.find_element(By.ID, "customer.ssn").send_keys("1783-7978-7876589")

    # Generate a unique username
    unique_username = f"kaspu{datetime.now().strftime('1478')}"
    driver.find_element(By.ID, "customer.username").send_keys(unique_username)
    driver.find_element(By.ID, "customer.password").send_keys("securePassword123")
    driver.find_element(By.ID, "repeatedPassword").send_keys("securePassword123")

    print("Submitting the registration form...")
    register_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))
    )
    register_button.click()

    print("Waiting for registration confirmation...")
    try:
        success_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )
        print("Registration succeeded:", success_message.text)
    except Exception:
        error_message = driver.find_element(By.CSS_SELECTOR, ".error").text
        print("Error during registration:", error_message)

finally:
    print("Closing the browser...")
    driver.quit()
