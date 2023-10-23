import requests

# Set the API endpoint URL and your OAuth token
url = 'https://utexas.instructure.com/api/v1/courses/<courseID>/assignments'  

# 'Authorization': 'Bearer <Canvas Authorization Token>',
headers = { 
    'Authorization': 'Bearer <Canvas Authorization Token>',
}


while url:
    # Make a GET request to the current URL
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for item in data:
            try:
                print("Name:", item['name'])
            except KeyError as e: #course is access restricted 
                print ("") 

        links = response.headers.get('Link')

        # get the next link
        next_link = None
        if links:
            links = links.split(',')
            for link in links:
                link_url, link_rel = map(str.strip, link.split(';'))
                if link_rel == 'rel="next"':
                    next_link = link_url.strip('<>')

        url = next_link
    else:
        print("Request failed with status code:", response.status_code)
        break
