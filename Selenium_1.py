from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome Profile
chrome_profile_path = "C:\\User Data"

#serv = Service(executable_path="chromedriver.exe")

# Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")

# Initialize the Chrome browser with the configured options
driver = webdriver.Chrome(options=chrome_options)
whats_url = "https://web.whatsapp.com"

def send_whatsapp_messages(messages=["Test Message"], phone_nums=[1234512345]):
    global i
    for i in range(0, len(phone_nums)):
        driver.get(whats_url+f"/send?phone={phone_nums[i]}")

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "_3Uu1_")))
        entry_field = driver.find_element(By.CLASS_NAME, "_3Uu1_")

        entry_field.send_keys(messages[i])
        entry_field.send_keys(Keys.ENTER)
        time.sleep(1)

def send_whatsapp_message(body="",num=""):
    driver.get(whats_url+f"/send?phone={num}")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "_3Uu1_")))
    entry_field = driver.find_element(By.CLASS_NAME, "_3Uu1_")
    entry_field.send_keys(body)
    entry_field.send_keys(Keys.ENTER)
    time.sleep(1)


'''
#print(len(nums))
#send_whatsapp_messages_to()
'''
#time.sleep(10)

driver.quit()