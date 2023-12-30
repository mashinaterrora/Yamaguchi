from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from online_sim import buy_number, receive_sms
from names import user_name, email
import time

options = webdriver.ChromeOptions()


s = Service(executable_path='D:\\Projects\\Yamaguchi\\chromedriver\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)


def main():
    try:
        driver.get(url="https://yamaguchi-massage.ru/pay/DS04012/1")
        time.sleep(1)

        phone_input = driver.find_element(By.XPATH, "/html/body/main/div/form/dl/div/input")
        phone_input.clear()
        phone_input.send_keys(buy_number())
        time.sleep(5)

        apply_phone_input = driver.find_element(By.XPATH, "/html/body/main/div/form/dl/button").click()
        time.sleep(10)

        code = receive_sms()
        print(code)
        for i in range(1, 5):
            code_input = driver.find_element(By.XPATH, f"/html/body/main/div/form/dd/fieldset/dl/div/input[{i}]")
            code_input.clear()
            code_input.send_keys(code[i])

        time.sleep(60)


        free_once_input = driver.find_element(By.XPATH, "/html/body/div/div/form[4]/button").click()
        time.sleep(1)

        reg_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/a").click()
        time.sleep(1)

        name_input = driver.find_element(By.ID, "name")
        name_input.clear()
        name_input.send_keys(user_name(10))
        time.sleep(1)

        email_input = driver.find_element(By.ID, "email")
        email_input.clear()
        email_input.send_keys(email(10))
        time.sleep(3)

        phone_input = driver.find_element(By.ID, "phone")
        phone_input.clear()
        phone_input.send_keys(buy_number())

        time.sleep(10)

        apply_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/dl/button").click()

        time.sleep(25)

        code_input = driver.find_element(By.XPATH, "/html/body/div/div/form/dl/label/input")
        code_input.clear()
        code_input.send_keys(receive_sms())

        time.sleep(20)

        apply_massage = driver.find_element(By.XPATH, "/html/body/div/div/form/dl/button").click()

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()
