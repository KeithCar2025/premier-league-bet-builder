import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API Key from the environment
API_KEY = os.getenv('FOOTBALL_DATA_API_KEY')

def test_api_connection():
    if not API_KEY:
        print('Error: FOOTBALL_DATA_API_KEY not found in .env file')
        return
    
    url = 'https://api.football-data.org/v2/competitions'
    headers = {'X-Auth-Token': API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print('✅ API connection successful!')
            data = response.json()
            print(f'Found {data["count"]} competitions')
        else:
            print(f'❌ API connection failed! Status code: {response.status_code}')
            print(f'Response: {response.text}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    test_api_connection()