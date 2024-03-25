import requests

endpoint = 'https://httpbin.org/'

get_response= requests.get(endpoint)
print(get_response.text)

# normal http request ==> HTML
# rest api http request ==>json