import requests

def get_appdetails(app_id):

    # the request will return data for a specified steam appId 
    url = f"https://store.steampowered.com/api/appdetails?cc=de&appids={app_id}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error retrieving data:", response.status_code)
        return {}
    
    app_data = response.json().get(f"{app_id}", [])

    if not app_data.get("success", False):
        print(f"No data for AppID {app_id} found.")
        return {}
    
    return app_data.get("data", {})

# returns just a name of a requested app 
def get_appdetails_name(app_id):
    return get_appdetails(app_id)['name']

# returns a dictionary with price information of a requested app 
# also returns the name, discount percent, final price, original price, currency and a link to the steam store page
def get_appdetails_price_info(app_id):
    price_info = get_appdetails(app_id).get("price_overview", None)
    if price_info:
        return {
            "name": get_appdetails(app_id).get("name"),
            "discount_percent": price_info.get("discount_percent"),
            "final_price": price_info.get("final") / 100,
            "original_price": price_info.get("initial") / 100,
            "currency": price_info.get("currency"),
            "steam_url": f"<https://store.steampowered.com/app/{app_id}>"
        }
    return {}
