import requests
import json
import os
import time
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
service = "yamaguchi"
country = 7


def buy_number():
    full_url = f"https://onlinesim.io/api/getNum.php?apikey={API_KEY}&service={service}&country={country}&number=true&lang=ru"

    response = requests.get(url=full_url)
    print(response.text)

    print(f"{response.status_code} {response.reason}")
    return json.loads(response.text)["number"][2:], json.loads(response.text)["tzid"]


def receive_sms():

    full_url = f"https://onlinesim.io/api/getState.php?apikey={API_KEY}&message_to_code=1&orderby=asc&msg_list=0&lang=ru"
    timing = time.time()

    while time.time() - timing < 30:
        req = requests.get(url=full_url)
        time.sleep(1)
        try:
            return json.loads(req.text)[-1]["msg"]
        except KeyError:
            print("Код не пришёл")


def check_balance():
    full_url = f"https://onlinesim.io/api/getBalance.php?apikey={API_KEY}&income=boolean&lang=ru"

    req = requests.get(url=full_url)

    if float(json.loads(req.text)["balance"]) < 0.06:
        return False
    else:
        return True


def set_operation_ok(tzid: list):

    full_url = f"https://onlinesim.io/api/setOperationOk.php?apikey={API_KEY}&tzid={tzid[0]}&lang=ru"

    req = requests.get(url=full_url)

    return json.loads(req.text)

