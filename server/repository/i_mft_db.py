from abc import ABCMeta, abstractmethod
from typing import List


class IMftDb(metaclass=ABCMeta):
    @abstractmethod
    def get_lenses(self) -> List[str]:
        pass
