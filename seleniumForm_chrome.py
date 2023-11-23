from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time



url = "https://whatismybrowser.com/detect/what-is-my-user-agent"

options = webdriver.ChromeOptions()


s = Service(executable_path='D:\\Projects\\Yamaguchi\\chromedriver\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
try:
    driver.get(url="https://vk.com/login")
    time.sleep(5)

    email_input = driver.find_element("id", "index_email")
    email_input.clear()
    email_input.send_keys("79623618753")
    time.sleep(5)
    email_input.send_keys(Keys.ENTER)

    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
