import requests
import json
import time
import time
from api_key import api_key


service = "yamaguchi"
country = 7


def buy_number():
    full_url = f"https://onlinesim.io/api/getNum.php?apikey={api_key}&service={service}&country={country}&number=true&lang=ru"

    response = requests.get(url=full_url)
    print(response.text)

    print(f"{response.status_code} {response.reason}")
    return json.loads(response.text)["number"]


def receive_sms():

    full_url = f"https://onlinesim.io/api/getState.php?apikey={api_key}&message_to_code=1&orderby=asc&msg_list=0&lang=ru"
    timing = time.time()

    while time.time() - timing < 30:
        req = requests.get(url=full_url)
        time.sleep(1)
        try:
            req = json.loads(req.text)[0]["msg"]
        except KeyError:
            print("Код не пришёл")
        finally:
            return req

