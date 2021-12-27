import discord
import time
import json
import os
from dotenv import load_dotenv
from discord import message, channel
from discord.ext import tasks
from requests.api import delete
from KijijiScraperCog import KijijiScraper

#inv --- https://discord.com/api/oauth2/authorize?client_id=924761663071207506&permissions=537127952&scope=bot

load_dotenv()

token = os.getenv('TOKEN')
client = discord.Client()
updates = client.fetch_channel('605133898552180736')

@client.event
async def on_ready():
    print(f'{client.user} has logged in!')



async def Update(channel):
    await KijijiScraper(channel)

async def DeleteAllMsg(channel):
    print('Starting to delete all messages')
    messages = await channel.history(limit=100).flatten()
    for message in messages:
        await message.delete()
        time.sleep(1)
    print('Bing! Done!')

async def AddNewUrl(message):
    incoming_message = message.content.split()
    url = incoming_message[1]
    with open('urls.txt', 'r') as file:
        lst = json.loads(file.read())
        if url in lst:
            print('URL is already in database!')

        if  'https://www.kijiji.ca/' in url and url not in lst:
            lst.append(url)
            with open('urls.txt', 'w') as file_write:
                file_write.write(json.dumps(lst))
                print('URL added to database')
        print(lst)

@client.event
async def on_message(message):
    if message.content.startswith('!update'):
        await Update(message.channel)

    if message.content.startswith('!delete_all'):
        await DeleteAllMsg(message.channel)
    
    if message.content.startswith('!start'):
        await AutoUpdate.start(message.channel)
        print('Sraper Started')
    
    if message.content.startswith('!add_url'):
        await AddNewUrl(message)

    if message.content.startswith('!help'):
            await message.reply('''List Of Commands
            !start ------ Starts the auto Webscraper
            !add_url ---- Adds new search URL (Must be a kijiji link)
            !delete_all - Deletes All messages in the server
            !update ----- Updates the Scraper
            ''')
            time.sleep(5)
        
        
    

@tasks.loop(hours=12)
async def AutoUpdate(channel):
    print('Starting Scraper!')
    await DeleteAllMsg(channel)
    print('Finished Deleting!')
    await Update(channel)
    print('Scraper up to date')



client.run(token)