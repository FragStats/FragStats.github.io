import requests

API_KEY = "your_api_key"
STEAM_ID = "DF49C4D882FE9530A497F7AFD86D196F"

def get_player_stats():
    url = f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={API_KEY}&steamid={STEAM_ID}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stats = data["playerstats"]["stats"]
        return {
            "total_kills": next(item["value"] for item in stats if item["name"] == "total_kills"),
            "total_deaths": next(item["value"] for item in stats if item["name"] == "total_deaths"),
            "total_rounds_played": next(item["value"] for item in stats if item["name"] == "total_rounds_played"),
            # Añadir más estadísticas según sea necesario
        }
    else:
        raise Exception("Error getting player stats from Steam API")
