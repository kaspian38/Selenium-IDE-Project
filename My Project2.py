# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMyProject():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_myProject(self):
    self.driver.get("https://webdriveruniversity.com/Contact-Us/contactus.html")
    self.driver.find_element(By.NAME, "first_name").click()
    self.driver.find_element(By.NAME, "first_name").send_keys("Kaspian")
    self.driver.find_element(By.NAME, "last_name").click()
    self.driver.find_element(By.NAME, "last_name").send_keys("Raihan")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("kaspian.raihan5226@gmail.com")
    self.driver.find_element(By.NAME, "message").click()
    self.driver.find_element(By.NAME, "message").send_keys("Hi, Kaspian Raihan. I forgot my university student portal user password.Please give me my student portal password.")
    self.driver.find_element(By.CSS_SELECTOR, ".contact_button:nth-child(2)").click()
  
