import time
import requests
from bs4 import BeautifulSoup
from requests.models import ChunkedEncodingError
from kijijiScraper import FindPathfinder


minute = 60
hour = minute * 60

def Main():
    run = True
    while run:
        client = time.localtime()

        cDay = client[2]
        cHour = client[3]
        cMin = client[4]
        cSec = client[5]
        FindPathfinder()
        print(f'Day: {cDay} @ {cHour}:{cMin}.{cSec}')
        time.sleep(2*hour)



if __name__ == '__main__':
    Main()