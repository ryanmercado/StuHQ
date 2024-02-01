import requests
import time
from typing import List


def getUpcomingAssignments(token:str):
    url = 'https://utexas.instructure.com/api/v1/users/self/upcoming_events'
    headers = {'Authorization': 'Bearer ' + token,}
    assignment_array = []
    while url:
            response = requests.get(url, headers=headers)

            if response.status_code == 403:  # Rate limit exceeded
                reset_time = int(response.headers.get('X-RateLimit-Reset', 60))  # Use a default value if not present
                print("Rate limit exceeded. Waiting for reset...")
                time.sleep(reset_time)
                continue  # Retry the request

            if response.status_code == 200:
                data = response.json()

                for item in data:
                    if "assignment" in item:
                        assignment_array.append(item["assignment"])

                links = response.headers.get('Link')

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
                print("URL:", url)
                print("Response content:", response.content)
                break
    return assignment_array

def getUpcomingEvents(token:str):
    url = 'https://utexas.instructure.com/api/v1/users/self/upcoming_events'
    headers = {'Authorization': 'Bearer ' + token,}
    event_array = []
    while url:
            response = requests.get(url, headers=headers)

            if response.status_code == 403:  # Rate limit exceeded
                reset_time = int(response.headers.get('X-RateLimit-Reset', 60))  # Use a default value if not present
                print("Rate limit exceeded. Waiting for reset...")
                time.sleep(reset_time)
                continue  # Retry the request

            if response.status_code == 200:
                data = response.json()

                for item in data:
                    if "assignment" not in item:
                        event_array.append(item)

                links = response.headers.get('Link')

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
                print("URL:", url)
                print("Response content:", response.content)
                break
    return event_array


def getAllCourses(token:str):
    # Set the API endpoint URL and your OAuth token
    url = 'https://utexas.instructure.com/api/v1/courses'  
    # 'Authorization': 'Bearer <Canvas Authorization Token>',
    headers = { 
        'Authorization': 'Bearer ' + token,
    }

    id_array = []

    while url:
        # Make a GET request to the current URL
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            for item in data:
                try:
                    id_array.append(item["id"])
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
    return id_array


def getCourse(id:str, token:str):
    # Set the API endpoint URL and your OAuth token
    url = 'https://utexas.instructure.com/api/v1/courses'  
    # 'Authorization': 'Bearer <Canvas Authorization Token>',
    headers = { 
        'Authorization': 'Bearer ' + token,
    }

    while url:
        # Make a GET request to the current URL
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            for item in data:
                if(item["id"] == id):
                    return item

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
