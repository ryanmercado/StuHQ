import requests

url = 'https://utexas.instructure.com/api/v1/courses'  

# 'Authorization': 'Bearer <Canvas Authorization Token>',
headers = {
    'Authorization': 'Bearer <Canvas User Authentication Token>',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print (data[0])

else:
    print("Request failed with status code:", response.status_code)
