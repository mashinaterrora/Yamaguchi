from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from online_sim import (
    buy_number,
    receive_sms,
    set_operation_ok
)
from names import user_name, email
import time

options = webdriver.ChromeOptions()


s = Service(executable_path='D:\\Projects\\Yamaguchi\\chromedriver\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)


def main():
    ids = []

    try:
        driver.get(url="https://yamaguchi-massage.ru/pay/DS04012/1")
        time.sleep(1)

        phone_input = driver.find_element(By.XPATH, "/html/body/main/div/form/dl/div/input")
        phone_input.clear()
        bought_number = buy_number()
        ids.append(bought_number[1])
        phone_input.send_keys(bought_number[0])
        time.sleep(5)

        apply_phone_input = driver.find_element(By.XPATH, "/html/body/main/div/form/dl/button").click()
        time.sleep(2)


        code = receive_sms()
        time.sleep(2)
        print(code)
        print(ids)


        code_input = driver.find_element(By.XPATH, f"/html/body/main/div/form/dd/fieldset/dl/div/input[1]")
        code_input.clear()
        code_input.send_keys(code[0])
        time.sleep(1)

        code_input = driver.find_element(By.XPATH, f"/html/body/main/div/form/dd/fieldset/dl/div/input[2]")
        code_input.clear()
        code_input.send_keys(code[1])
        time.sleep(1)

        code_input = driver.find_element(By.XPATH, f"/html/body/main/div/form/dd/fieldset/dl/div/input[3]")
        code_input.clear()
        code_input.send_keys(code[2])
        time.sleep(1)

        code_input = driver.find_element(By.XPATH, f"/html/body/main/div/form/dd/fieldset/dl/div/input[4]")
        code_input.clear()
        code_input.send_keys(code[3])
        time.sleep(1)

        time.sleep(5)

        apply_code_input = driver.find_element(By.XPATH, "/html/body/main/div/form/dd/fieldset/dl/button").click()
        time.sleep(1)


        name_input = driver.find_element(By.XPATH, "/html/body/main/div/form/dl/div[1]/div[1]/input")
        name_input.clear()
        name_input.send_keys(user_name(10))
        time.sleep(1)

        email_input = driver.find_element(By.XPATH, "/html/body/main/div/form/dl/div[1]/div[2]/input")
        email_input.clear()
        email_input.send_keys(email(10))
        time.sleep(1)

        time.sleep(2)


        apply_massage = driver.find_element(By.XPATH, "/html/body/main/div/form/dl/button").click()

        time.sleep(2)

        apply_10_minutes = driver.find_element(By.XPATH, "/html/body/main/div/ul/li[4]/form/button").click()

        time.sleep(10)

        print(set_operation_ok(ids))

        time.sleep(5)



    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()
