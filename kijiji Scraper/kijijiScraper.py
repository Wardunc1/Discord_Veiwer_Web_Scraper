from bs4 import BeautifulSoup
import requests
  
def FindPathfinder():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/nissan-pathfinder/k0c174l1700203?ll=53.546125%2C-113.493823&for-sale-by=ownr&address=Edmonton%2C+AB&radius=520.0&price=__2000'
    page = requests.get(myurl)

    soup = BeautifulSoup(page.content,'html.parser')

    results = soup.find(id = 'MainContainer')

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


        print('----------------')
        print(title.text.strip())
        print(f'https://www.kijiji.ca/{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')

if __name__ == '__main__':
    FindPathfinder()
    
   
