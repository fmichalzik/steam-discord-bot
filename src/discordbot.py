import os
from dotenv import load_dotenv
import discord
from topsellers import message_discounted_topsellers

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable not set.")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Ahoy!')

    if message.content.startswith('!topseller'):
        await message.channel.send("Du sucht also nach Schätzen, aye? Gib' mir 'ne Sekunde ...")
        await message.channel.send(message_discounted_topsellers())

client.run(TOKEN)