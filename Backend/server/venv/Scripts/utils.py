import requests

lichess_api_url = "https://lichess.org/api/"

def get_top_players():
    response = requests.get(f"{lichess_api_url}player/top/50")
    if response.status_code == 200:
        top_players = response.json()
        return top_players
    else:
        return None

def get_player_rating_history(username):
    response = requests.get(f"{lichess_api_url}user/{username}/rating-history")
    if response.status_code == 200:
        rating_history = response.json()
        return rating_history
    else:
        return None
