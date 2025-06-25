import requests
from appdetails import get_appdetails_price_info

def get_topsellers(count=1):
    
    # the request will return unfortunally just return a json with the name and a logo link
    # however the logo link also contains the appID which can be used later
    # if the count <= 25 it well always return at least 25 results  
    url = f"https://store.steampowered.com/search/results/?count={count}&filter=topsellers&hidef2p=1&json=1"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error retrieving data:", response.status_code)
        return []
    
    return response.json().get("items", [])

# returns a list with just the names of the topsellers 
def get_topsellers_names(count=1):
    topsellers = get_topsellers(count)
    names = []
    for topseller in topsellers:
        names.append(topseller['name'])
    return names

# returns a list with just the ids of the topsellers 
def get_topsellers_ids(count=1):
    topsellers = get_topsellers(count)
    ids = []
    for topseller in topsellers:
        id = topseller['logo'].split("/")[6]
        ids.append(id)
    return ids

def get_discounted_topsellers(count=1, discount=33):
    discounted_topsellers = []
    topsellers_ids = get_topsellers_ids(count)
    for topseller_id in topsellers_ids:
        topseller = get_appdetails_price_info(topseller_id)
        if topseller['discount_percent'] >= discount:
            discounted_topsellers.append(topseller)
    return discounted_topsellers

def print_discounted_topsellers(count=1, discount=33):
    discounted_topsellers = get_discounted_topsellers(count, discount)
    print(
f'''
🎮 Aktuelle Steam-Topseller mit mindestens {discount}% Rabatt: {len(discounted_topsellers)}
        
''')
    for game in discounted_topsellers:
        print(
f'''
{game['name']} - {game['discount_percent']}% Rabatt
Preis: {game['final_price']}€ (statt {game['original_price']}€)
Link: {game['steam_url']}

'''
        )