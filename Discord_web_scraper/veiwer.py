import discord
from discord import message 
from findPathFinder import KijijiScraper


token = 'ODU0MTE2ODkzNjc2Nzk3OTUy.YMfQWA.bY_WFdtqJePNToNBemsemmYPf3Y'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has logged in!')


async def Update(message):
    await KijijiScraper(message)


@client.event
async def on_message(message):
    if message.content.startswith('!update'):
        await Update(message)


client.run(token)