from bs4 import BeautifulSoup
import requests
class Place:
    def __init__(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
        responce = requests.get("https://www.zillow.com/london-ky/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Ukiah%2C%20CA%22%2C%22mapBounds%22%3A%7B%22north%22%3A37.410445434990585%2C%22east%22%3A-83.49019681835937%2C%22south%22%3A36.73770030711285%2C%22west%22%3A-84.65749418164062%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A53028%2C%22regionType%22%3A6%7D%5D%2C%22category%22%3A%22cat1%22%7D", headers=header)
        # print(responce.text)
        soup = BeautifulSoup(responce.text, "html.parser")
        link = soup.select(selector=" #grid-search-results > ul > li > div > div > article > div > div.StyledPropertyCardDataWrapper-c11n-8-85-1__sc-1omp4c3-0.jVBMsP.property-card-data > a")
        price = soup.select(selector="#grid-search-results > ul > li > div > div > article > div > div.StyledPropertyCardDataWrapper-c11n-8-85-1__sc-1omp4c3-0.jVBMsP.property-card-data > div.StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0.bqsBln > span",)
        self.list_data = []
        for x in range(0,len(link)):
            div = { "add":link[x].string,
                    "link":link[x].get("href"),
                    "price":price[x].string}
            self.list_data.append(div)

