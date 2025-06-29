import requests
from appdetails import get_appdetails_release_date

def get_games_by_name(game_name):
    input = game_name.split(" ")
    term = "+".join(input)
    url = f"https://store.steampowered.com/api/storesearch/?term={term}&l=german&cc=DE"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error retrieving data:", response.status_code)
        return []
    
    return response.json().get("items", [])

# generated a formatted print out for the get_discounted_topsellers functions
def message_games_by_name(game_name):
    games = get_games_by_name(game_name)
    if not games:
        return "Da find' ich nichts ..."
    message = (
f'''
🔍 Schau mal was ich gefunden habe:   
''')
    for game in games:
        message += (
f'''
{game['name']} - ID {game['id']}
Preis: {game.get('price', {}).get('final', 0)/100}€   Metascore: {game['metascore']} 
Link: <https://store.steampowered.com/app/{game['id']}>
'''
    )
        release_date = get_appdetails_release_date(game['id'])
        if release_date:
            message += (
f'''Release: {release_date}
''')
    
    return message