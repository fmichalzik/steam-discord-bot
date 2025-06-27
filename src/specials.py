import requests

# the call to the api will always just return 10 results
def get_specials():
    url = f"https://store.steampowered.com/api/featuredcategories?cc=de"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error retrieving data:", response.status_code)
        return []
    
    return response.json().get("specials", []).get("items", {})

# generated a formatted print out for the get_discounted_topsellers functions
def message_specials():
    specials = get_specials()
    if not specials:
        return "Ich find' gerade nichts, hau mal den Captain an!"
    message = (
f'''
⭐ Aktuelle Steam-Specials !!!       
''')
    for game in specials:
        message += (
f'''
{game['name']} - {game['discount_percent']}% Rabatt
Preis: {game['final_price']/100}€ (statt {game['original_price']/100}€)
Link: <https://store.steampowered.com/app/{game['id']}>

'''
        )
    
    return message