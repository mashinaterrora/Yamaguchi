import requests
import json
import time
from api_key import api_key


service = "yamaguchi"
country = 7
# Extract parameters from the options object

def buy_number():

    fullUrl = f"https://onlinesim.io/api/getNum.php?apikey={api_key}&service={service}&country={country}&number=true&lang=ru"

    method = "GET"

    mimeType = "application/x-www-form-urlencoded"
    
    response = requests.get(url=fullUrl)
    print(response.text)

    # req = requests.Request(method, fullUrl, headers=headers, cookies=cookies)

    # if postData:
    #     req.data = postData

    # prepared_req = req.prepare()

    # session = requests.Session()
    # response = session.send(prepared_req)
 
    print(f"{response.status_code} {response.reason}")
    return json.loads(response.text)["number"]
    


def receive_sms():

    fullUrl = f"https://onlinesim.io/api/getState.php?apikey={api_key}&message_to_code=1&orderby=asc&msg_list=0&lang=ru"


    method = "GET"

    mimeType = "application/x-www-form-urlencoded"

    # req = requests.get(url=fullUrl, headers=headers, cookies=cookies)
    # print('Hui', req.text)

    req = requests.get(url=fullUrl)
    try:
        req = json.loads(req.text)[0]["msg"]
    except KeyError:
        print("Код не пришёл")
    finally:
    # print(req)
    # while req == "TZ_NUM_WAIT" or req == "ERROR_NO_OPERATIONS":
    #     req = requests.get(url=fullUrl)
    #     time.sleep(3)
        return req 
        
    
    # return json.loads(response.text)[0]["response"]

def find_number():
    fullUrl = f"https://onlinesim.io/api/getState.php?apikey={api_key}&message_to_code=1&orderby=asc&msg_list=1&clean=1&lang=ru"

    method = "GET"

    mimeType = "application/x-www-form-urlencoded"
    headers = {
        
    }
    postData = {
    }
    cookies = {
        
    }
    # req = requests.get(url=fullUrl, headers=headers, cookies=cookies)
    # print('Hui', req.text)
    # Set up the request
    req = requests.Request(method, fullUrl, headers=headers, cookies=cookies)
    # Add data to the request
    if postData:
        req.data = postData
    # Construct the prepared request
    prepared_req = req.prepare()
    # Send the request and get the response
    session = requests.Session()
    response = session.send(prepared_req)
    # Handle the response
    print(f"{response.status_code} {response.reason}")
    return json.loads(response.text)[0]["number"]
    # Handle errors
    if response.status_code >= 400:
        print("Error:", response.status_code, response.reason)



receive_sms()
