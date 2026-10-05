from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
load_dotenv()

email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
number = os.environ["NUMBER"]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")
main_window = driver.current_window_handle

time.sleep(80)




time.sleep(3)


time.sleep(4)
swipe = True
while swipe:
    try:

        like_button = driver.find_element(By.XPATH, '//button//span[text()="Like"]')
        driver.execute_script("arguments[0].click()", like_button)
        print("Liked")
        time.sleep(2)

    except:
        print("Fail")
