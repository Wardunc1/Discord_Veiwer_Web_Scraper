from bs4 import BeautifulSoup
import requests
import discord
import time
import json


async def KijijiScraper(channel):
    with open('urls.txt', 'r') as file:
        urls = json.loads(file.read())
        for url in urls:
            myurl = url
            page = requests.get(myurl)

            soup = BeautifulSoup(page.content,'html.parser')

            results = soup.find(id = 'MainContainer')

            messages = []
            
            listings = results.find_all('div', class_= 'search-item')
            listings_found = len(listings)

            for listing in listings:

                title_tag = listing.find('div', class_ = 'title')
                title = title_tag.find('a')
                weburl = title['href']

                price = listing.find('div', class_='price')

                location_tag = listing.find('div', class_='location')
                location = location_tag.find('span')

                datePosted = location_tag.find('span', class_='date-posted')

                msg = f'''----------------
        {title.text.strip()}
        https://www.kijiji.ca{weburl}
        {price.text.strip()}
        {location.text.strip()}
        {datePosted.text.strip()}
        ''' 
                await channel.send(msg)
                time.sleep(0.25)
            if listings_found >= 1:
                text = f'''----------------
            {listings_found} Listings Found
            ----------------'''
                await channel.send(text)
                time.sleep(0.25)
    
