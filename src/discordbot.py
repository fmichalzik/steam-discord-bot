import os
from dotenv import load_dotenv
import discord
from topsellers import message_discounted_topsellers
from specials import message_specials
from keywords import GREETINGS
from search import message_games_by_name

##### SETUP FOR THE BOT #####

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable not set.")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

##### CONTROLLING FOR THE BOT #####

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user}')

##### ON MESSAGE ACTIONS #####

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!help'):
            help_response = (
f'''Was kann ich für Euch tun, Matrose?
- !topseller count discount
- !specials
- !search xy
''')
            await message.channel.send(help_response)
    
    for greeting in GREETINGS:
        if message.content.startswith(greeting):
            await message.channel.send('Ahoy!')

    if message.content.startswith('!specials'):
        await message.channel.send("Was Besonderes, mhm? Na mal sehen ...")
        await message.channel.send(message_specials())

    if message.content.startswith('!search'):
        # Ganze Nachricht aufteilen in keyword !search und was danach kommt (gamename)
        parts = message.content.split(' ', 1)
        if len(parts) < 2:
            await message.channel.send("Wonach soll ich suchen ? z.B. `!search Republic of Pirates`")
            return
        game_name = parts[1]  # Alles nach !search
        await message.channel.send(message_games_by_name(game_name))

    if message.content.startswith('!topseller'):
        await message.channel.send("Du sucht also nach Schätzen, aye? Gib' mir 'ne Sekunde ...")
        parts = message.content.split(' ')
        if len(parts) != 3:
            await message.channel.send(message_discounted_topsellers())
        else:
            await message.channel.send(message_discounted_topsellers(int(parts[1]), int(parts[2])))

client.run(TOKEN)