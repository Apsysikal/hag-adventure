from abc import ABC, abstractmethod

class GameComponent(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass