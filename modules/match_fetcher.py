import requests

class MatchFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.football-data.org/v2/'

    def fetch_premier_league_matches(self):
        url = f"{self.base_url}competitions/PL/matches"
        headers = {
            'X-Auth-Token': self.api_key
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None  # or raise an error or return a message
