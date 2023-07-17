from abc import ABC, abstractmethod


class Scrapper(ABC):
    @abstractmethod
    def scrape_method(self) -> str:
        pass
