import requests
import json
# Extract parameters from the options object



fullUrl = f"https://onlinesim.io/api/getNumbersStats.php?country=7&lang=ru"
method = "GET"
mimeType = "application/x-www-form-urlencoded"
headers = {
    
}
postData = {
}
cookies = {
    
}
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

response = json.loads(response.text)

print(response)
# print(response.text)
# Handle errors
if response.status_code >= 400:
    print("Error:", response.status_code, response.reason)
