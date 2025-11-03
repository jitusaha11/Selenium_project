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
page_url = "https://www.instagram.com/ldu_oficial/"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)


driver.get("https://www.instagram.com/?flo=true")
time.sleep(4)


wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)


driver.find_element(By.NAME, "password").send_keys(password + Keys.ENTER)

time.sleep(4)


driver.get(page_url)
time.sleep(5)

followers_text = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//ul/li[2]/a/div/span")
)).get_attribute("title")  

print("Followers text:", followers_text)


def convert_followers(text):
    text = text.lower().replace(",", "")

    if "k" in text:
        number = float(text.replace("k", "")) * 1000
    elif "m" in text:
        number = float(text.replace("m", "")) * 1000000
    else:
        number = float(text)
    return number


followers = convert_followers(followers_text)
print("Followers number:", followers)

if followers > 100:
    try:
        follow_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(translate(., 'FOLLOW', 'follow'), 'follow')])[1]")
        ))
        follow_btn.click()
        print(" Followed the page!")

        try:
            wait.until(EC.text_to_be_present_in_element(
                (By.XPATH, "(//button)[1]"), "Following"
            ))
            print("Button changed to FOLLOWING")

        except:
            print("Could not confirm button text but likely followed")

        time.sleep(10)

    except:
        print("Already following or Follow button not found.")
else:
    print("Followers are less than 100 — not following.")

time.sleep(10)
driver.quit()
