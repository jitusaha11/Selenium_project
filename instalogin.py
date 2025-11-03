from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


username = "edgar.navarro@suroscuraec.com"
password = "Ruhani@123"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)


driver.get("https://www.instagram.com/?flo=true")
time.sleep(4)


wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)

driver.find_element(By.NAME, "password").send_keys(password + Keys.ENTER)
wait = WebDriverWait(driver, 10)

time.sleep(10)
driver.quit()
