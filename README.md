# steam-discord-bot
First personal python project. <br>

The idea is to utilize API calls to recieve data from Steam and use the data for a discord bot to post stuff on a personal discord. 

### Initial Steps
- learning / understanding steams api (/)
- create the first api call function (like get topseller) (/)
- create a initial framework so additional call functions can be added later

- learn about discord bots
- setup a discord bot for a personal discord
- find a way "for the discord bot to youse the api call functions"


### Setup
Set up a virtual environment. Virtual environments are Python's way<br>
to keep dependencies separate from other projects on our machine.
```
python3 -m venv venv
source venv/bin/activate
```

Install the requirements.
```
pip install -r requirements.txt
```

### Functions

#### print_discounted_topsellers(count=1, discount=33)
count - defaults to 1. count <= 25 well get at least the top 25 topsellers. this list is then trimmed by...<br>
discount - defaults to 33
    
Example:
```
🎮 Gefundene Spiele mit mindestens 80% Rabatt: 5
        


STAR WARS™ Battlefront™ II - 90% Rabatt
Preis: 3.99€ (statt 39.99€)
Link: https://store.steampowered.com/app/1237950



EA SPORTS FC™ 25 - 80% Rabatt
Preis: 13.99€ (statt 69.99€)
Link: https://store.steampowered.com/app/2669320



theHunter: Call of the Wild™ - 80% Rabatt
Preis: 3.9€ (statt 19.5€)
Link: https://store.steampowered.com/app/518790



STAR WARS Jedi: Survivor™ - 80% Rabatt
Preis: 13.99€ (statt 69.99€)
Link: https://store.steampowered.com/app/1774580



Far Cry® 5 - 85% Rabatt
Preis: 8.99€ (statt 59.99€)
Link: https://store.steampowered.com/app/552520
```
