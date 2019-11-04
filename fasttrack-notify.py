from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
from notify_run import Notify
import time

page_url = "https://info.su.dk/UdlandWeb/FastTrackController?educationDegree=BACHELOR&country=DE&university=13994" \
           "&broadField=XX&educationField=XX "
# opens the connection and downloads html page from url
uClient = uReq(page_url)
notified: bool = False


def scrape():
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    found = page_soup.findAll("span", {"class": "emphasis"})

    if str(found[0]) != '<span class="emphasis">Intet fundet.</span>':
        notify_mikkel()


def notify_mikkel():
    notify = Notify(api_server='https://notify.run/api/', endpoint="https://notify.run/tgxHEXy7AVp1Ea6Q")
    notify.write_config()
    notify.send("Uddannelse fundet test")
    global notified
    notified = True


while True:
    if notified:
        print("Breaking")
        break
    else:
        print("scrape Time")
        scrape()
        time.sleep(300)
