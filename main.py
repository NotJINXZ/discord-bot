### Imports ###
import discord
import random
import asyncio
import datetime
import json
import os
import platform

### End Imports ###

### Config ###
if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]

### End Config ###

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True) 
client = MyClient(intents=intents, case_insensitive = True)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)