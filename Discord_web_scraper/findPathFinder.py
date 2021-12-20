from bs4 import BeautifulSoup
import requests
import discord
from urls import urls

async def KijijiScraper(message):
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

            messages.append(msg)

        text = ''''''

        for msg in messages:
            text += msg

        text += f'''----------------
    {listings_found} Listings Found
    ----------------'''
        await message.reply(text)
    
    #
  #      print('')
  #      print()
  #      print( ')
  #      print()
  #      print()
  #      print()
  #  print('----------------')
  #  print('----------------')
  #  print(f'{listings_found} Listings Found')
  #  print('----------------')
#