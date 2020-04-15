from selenium import webdriver
from selenium.webdriver.common.by import By #Util para algunos selectores
from selenium.webdriver.common.keys import Keys #Permite introducir texto
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pprint import pprint
from dotenv import load_dotenv

import sys, os, time
load_dotenv()
USERNAME = os.getenv('USERNAME_IG')
PASSWORD = os.getenv('PASSWORD_IG')

URL = "https://www.instagram.com/"

DRIVER_PATH = "/usr/bin/chromedriver"
BRAVE_BROWSER_PATH = "/usr/bin/brave-browser"

driver_options = webdriver.ChromeOptions()
driver_options.binary_location = BRAVE_BROWSER_PATH
driver_options.add_argument("--incognito")

browser = webdriver.Chrome(executable_path=DRIVER_PATH, options=driver_options)

# browser.set_page_load_timeout(7) #Esperara 7 segundos para que la pagina cargue
browser.implicitly_wait(10)
browser.get(URL)
browser.maximize_window()
# LOGIN
username_input = browser.find_element_by_name("username")
username_input.send_keys(USERNAME)

password_input = browser.find_element_by_name('password')
password_input.send_keys(PASSWORD)

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()

try:
  wait = WebDriverWait(browser, 10)
  # Para que busque el elemento se deben pasar los valores como tuplas
  selector = (By.CSS_SELECTOR, "div>button:last-of-type[tabindex='0']")
  not_now_btn = wait.until(EC.element_to_be_clickable(selector)).click()
except TimeoutException:
  print("Time to load took to mutch time")

for item in range(10):
  time.sleep(5)
  browser.execute_script("window.scrollTo({top:document.body.scrollHeight, behavior:'smooth'})")


browser.close()