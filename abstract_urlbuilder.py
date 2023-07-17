from abc import ABC, abstractmethod


class UrlBuilder(ABC):

    @abstractmethod
    def get_url(self) -> str:
        pass
