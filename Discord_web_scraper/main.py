import time
import requests
from bs4 import BeautifulSoup
from requests.models import ChunkedEncodingError
from kijijiScraper import *


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
        
        time.sleep(10)

        Find4Runner()

        time.sleep(10)

        FindOutBack()

        time.sleep(10)

        FindRav4()

        time.sleep(10)

        FindFrontier()

        time.sleep(10)

        FindXterra()

        time.sleep(10)

        FindTaccoma()

        time.sleep(10)

        FindJeep()

        time.sleep(10)

        FindFERDFCKNRANGER()

        time.sleep(10)

        FindLandCruiser()


        print(f'Day: {cDay} @ {cHour}:{cMin}.{cSec}')
        time.sleep((24 * hour) - (2 * minute))



if __name__ == '__main__':
    Main()