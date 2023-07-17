from abstract_scrapper import Scrapper
from abstract_urlbuilder import UrlBuilder
import asyncio
from typing import Type


class ExecuteScrapper:
    def __init__(self, symbols: list[str], country_code: str, urlbuilder: Type[UrlBuilder],
                 scrapper: Type[Scrapper]) -> None:
        self.symbols = symbols
        self.country_code = country_code
        self.urlbuilder = urlbuilder
        self.scrapper = scrapper

    async def scrape_tasks(self) -> list:
        tasks = []
        for symbol in self.symbols:
            urlobject = self.urlbuilder(symbol, self.country_code)
            tasks.append(self.scrapper(urlobject).scrape_method())
        return tasks

    async def execute_scrapping(self) -> list[str]:
        tasks = await self.scrape_tasks()
        responses = await asyncio.gather(*tasks)
        return responses
