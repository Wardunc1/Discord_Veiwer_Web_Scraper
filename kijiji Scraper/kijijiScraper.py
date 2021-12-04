from bs4 import BeautifulSoup
import requests
  
def FindPathfinder():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/nissan-pathfinder/__2000/k0c174l1700203a68?ll=53.546125%2C-113.493823&for-sale-by=ownr&address=Edmonton%2C+AB&radius=520.0&price=__2000'
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
        print(f'https://www.kijiji.ca{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')

def FindRav4():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/rav4/__2000/k0c174l1700203a68?rb=true&ll=53.546125%2C-113.493823&for-sale-by=ownr&address=Edmonton%2C+AB&price=__2000&radius=520.0'
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
        print(f'https://www.kijiji.ca{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')

def FindOutBack():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/subaru-outback/__2000/k0c174l1700203a68?rb=true&ll=53.546125%2C-113.493823&for-sale-by=ownr&address=Edmonton%2C+AB&price=__2000&radius=520.0'
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
        print(f'https://www.kijiji.ca{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')



def Find4Runner():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/toyota-4runner/__2000/k0c174l1700203a68?radius=520.0&ad=offering&price=__2000&address=Edmonton%2C+AB&ll=53.546125,-113.493823&for-sale-by=ownr'
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
        print(f'https://www.kijiji.ca{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')

def FindFrontier():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/nissan-frontier/__2000/k0c174l1700203a68?rb=true&ll=53.546125%2C-113.493823&for-sale-by=ownr&address=Edmonton%2C+AB&price=__2000&radius=520.0'
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
        print(f'https://www.kijiji.ca{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')

def FindXterra():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/nissan-xterra/__2000/k0c174l1700203a68?rb=true&ll=53.546125%2C-113.493823&for-sale-by=ownr&address=Edmonton%2C+AB&price=__2000&radius=520.0'
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
        print(f'https://www.kijiji.ca{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')

def FindTaccoma():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/toyota-tacoma/__2000/k0c174l1700203a68?rb=true&ll=53.546125%2C-113.493823&for-sale-by=ownr&address=Edmonton%2C+AB&price=__2000&radius=520.0'
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
        print(f'https://www.kijiji.ca{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')

def FindJeep():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/jeep-cherokee/__2000/k0c174l1700203a68?rb=true&ll=53.546125%2C-113.493823&for-sale-by=ownr&address=Edmonton%2C+AB&price=__2000&radius=520.0'
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
        print(f'https://www.kijiji.ca{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')

def FindFERDFCKNRANGER():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/ford-ranger/__2000/k0c174l1700203a68?rb=true&ll=53.546125%2C-113.493823&for-sale-by=ownr&address=Edmonton%2C+AB&price=__2000&radius=520.0'
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
        print(f'https://www.kijiji.ca{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')


def FindLandCruiser():

    myurl = 'https://www.kijiji.ca/b-cars-trucks/edmonton/toyota-land-cruiser/__2000/k0c174l1700203a68?rb=true&ll=53.546125%2C-113.493823&for-sale-by=ownr&address=Edmonton%2C+AB&price=__2000&radius=520.0'
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
        print(f'https://www.kijiji.ca{weburl} ')
        print(price.text.strip())
        print(location.text.strip())
        print(datePosted.text.strip())
    print('----------------')
    print(f'{listings_found} Listings Found')
    print('----------------')



    
