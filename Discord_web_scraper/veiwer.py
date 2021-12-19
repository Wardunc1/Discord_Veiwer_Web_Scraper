import discord
from discord import message 
import main as main


token = 'ODU0MTE2ODkzNjc2Nzk3OTUy.YMfQWA.bY_WFdtqJePNToNBemsemmYPf3Y'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has logged in!')


async def Update():
    main.Main()

@client.event
async def on_message(message):
    if message.content.startswith('!update'):
        await Update()

client.run(token)