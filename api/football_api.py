# Football API Integration

import requests

class FootballAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.football-data.org/v2/'

    def get_leagues(self):
        response = requests.get(f'{self.base_url}leagues', headers={'X-Auth-Token': self.api_key})
        return response.json()

    def get_matches(self, league_id):
        response = requests.get(f'{self.base_url}matches?leagueId={league_id}', headers={'X-Auth-Token': self.api_key})
        return response.json()