import asyncio
from abstract_scrapper import Scrapper
from abstract_urlbuilder import UrlBuilder
from executescrapper import ExecuteScrapper
import aiohttp
from bs4 import BeautifulSoup


class MarketWatchUSUrl(UrlBuilder):
    def __init__(self, key: str, country_code: str):
        self.key = key
        self.country_code = country_code

    def get_url(self):
        url = rf"https://www.marketwatch.com/investing/stock/{self.key.lower()}/company-profile?mod=mw_quote_tab"
        return url


class MarketWatchUSScrapper(Scrapper):

    def __init__(self, urlbuilder: UrlBuilder) -> None:
        self.url = urlbuilder.get_url()

    async def scrape_method(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                response = await response.text()
                soup = BeautifulSoup(response, 'html.parser')
                description = soup.find('p', {'class':'description__text'}).text
        return description


if __name__ == "__main__":
    symbol_list = ["A", "B", "C"]
    country = "US"
    coroutine = ExecuteScrapper(symbol_list, country, MarketWatchUSUrl,
                                MarketWatchUSScrapper).execute_scrapping()
    execution_responses = asyncio.run(coroutine)

    for resp in execution_responses:
        print(resp)
