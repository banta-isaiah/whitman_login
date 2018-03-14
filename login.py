import requests
from lxml import html

username = "<username>"
password = "<password>"

login_url = "https://cas.whitman.edu/login"
url = "https://my.whitman.edu/students"

def main():
    session_requests = requests.session()

    # Get login csrf token
    print("Navigating to login_url...")
    result = session_requests.get(login_url)
    if (result.ok):
        print("Successful.")
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='lt']/@value")))[0]
    execution = list(set(tree.xpath("//input[@name='execution']/@value")))[0]
    _eventId = list(set(tree.xpath("//input[@name='_eventId']/@value")))[0]

    # Create payload
    payload = {
        "username": username, 
        "password": password, 
        "lt": authenticity_token,
        "execution": execution,
        "_eventId": _eventId
        }

    # Perform login
    print('Attempting to login...')
    result = session_requests.post(login_url, data = payload, headers = dict(referer=login_url))
    if (result.ok):
        print('Login successful!')
        

if __name__ == '__main__':
    main()
