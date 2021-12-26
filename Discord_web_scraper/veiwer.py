from enum import auto
from re import A
from aiohttp.tracing import TraceRequestChunkSentParams
import discord
from discord import message
from discord import channel 
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
        
        await AutoUpdate(updates)

@taskloop(0):
async def AutoUpdate(channel):
    run = True
    start = True
    while run:
        if start:
            print('Web Scraper Running')
            start = False

        if time.tm_hour == 12 and time.tm_min == 30:
            await DeleteAllMsg(channel)
            await Update(channel)


        if time.tm_hour == 15 and time.tm_min == 30:
            await DeleteAllMsg(channel)
            await Update(channel)
        
    
client.run(token)