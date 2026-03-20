import requests
import os

# Load API Key from the environment
API_KEY = os.getenv('API_KEY')

def test_api_connection():
    url = 'https://api.football-data.org/v2/'
    headers = {'X-Auth-Token': API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print('API connection successful!')
    else:
        print('API connection failed! Status code:', response.status_code)

if __name__ == '__main__':
    test_api_connection()