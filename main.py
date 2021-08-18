import random
import time
import urllib.request
import urllib.parse

# Didn't use requests 
# https://stackoverflow.com/questions/62684468/pythons-requests-triggers-cloudflares-security-while-urllib-does-not

# Recaptcha not needed for now
# Getting the token requires sending a payload
# along with the request that contains unique
# information on your browser and computer.

# def get_recaptcha_token(payload):
#     url = "https://google.com/recaptcha/api2/reload?k=6Ledv1IaAAAAAKFJSR7VKPE8e-4kht4ZmLzencES"
#     
#     request_data = urllib.parse.urlencode(payload)
#     request_data = request_data.encode("ascii")
# 
#     request = urllib.request.Request(url, data=request_data, headers=headers)
#     r = urllib.request.urlopen(request).read()
# 
#     # cookie = r.headers["Set-Cookie"].split(";")[0]
#     captcha_token = r.text.strip('][').split(',')[1].strip('"')
#     
#     return captcha_token


def send_clicks(params):
    url = "https://stats.popcat.click/pop"
    headers = (' {"Host": "stats.popcat.click", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",'
              ' "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Origin": "https://popcat.click",  '
              ' "Connection": "keep-alive", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Content-Type": "application/x-www-form-urlencoded" }')
    headers = eval(headers)

    # encode additional data into bytes for body
    request_data = urllib.parse.urlencode(params)
    request_data = request_data.encode("ascii")

    request = urllib.request.Request(url, data=request_data, headers=headers)
    r = urllib.request.urlopen(request).read()
    
    return r.decode("utf-8")


print("This is open source software. See LICENSE.")
print("This may take a minute to set up. If you get HTTP Error 429, make sure you"
      "do not have Popcat open anywhere else on your network.")
print("============================================================================")
print("Sending clicks to popcat on a 30-second interval. Press CTRL + C to stop me.")
print("============================================================================")

while True:
    params = dict()
    params["pop_count"] = random.randint(750, 800)
    params["captcha_token"] = "NULL"

    print("Sending", params["pop_count"], "clicks")

    try:
        response = send_clicks(params)
        print(response)
    except urllib.error.HTTPError as e:
        print(e)
        print("Trying again in 30 seconds")
    except:
        print("Unexpected error")
        raise

    time.sleep(30)
