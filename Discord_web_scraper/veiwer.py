import discord
from discord import message, channel
from discord.ext import tasks
from KijijiScraperCog import KijijiScraper
import time as time

token = 'ODU0MTE2ODkzNjc2Nzk3OTUy.YMfQWA.bY_WFdtqJePNToNBemsemmYPf3Y'
client = discord.Client()
t = time
time = t.localtime()
updates = client.fetch_channel('605133898552180736')

@client.event
async def on_ready():
    print(f'{client.user} has logged in!')



async def Update(channel):
    await KijijiScraper(channel)

async def DeleteAllMsg(channel):
    messages = await channel.history(limit=100).flatten()
    await channel.delete_messages(messages)

@client.event
async def on_message(message):
    if message.content.startswith('!update'):
        await Update(message.channel)
    
    if message.content.startswith('!time'):
        print(t.localtime())

    if message.content.startswith('!delete_all'):
        await DeleteAllMsg(message.channel)
    
    if message.content.startswith('!start'):
        await AutoUpdate.start(message.channel)
        print('Sraper Started')

@tasks.loop(hours=12)
async def AutoUpdate(channel):
    await DeleteAllMsg(channel)
    await Update(channel)

client.run(token)