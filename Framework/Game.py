from abc import ABC, abstractmethod
from typing import List

from Framework.GameComponent import GameComponent

class Game(ABC):
    _gameComponents: List[GameComponent]
    
    @abstractmethod
    def __init__(self):
        self._gameComponents = []

    @abstractmethod
    def initialize(self) -> None:
        for gameComponent in self._gameComponents:
            gameComponent.initialize()

    @abstractmethod
    def update(self) -> None:
        for gameComponent in self._gameComponents:
            gameComponent.update()

    def addComponent(self, component: GameComponent) -> None:
        if component in self._gameComponents: raise Exception(f"Cannot add component {component} twice")
        self._gameComponents.append(component)

    def removeComponent(self, component: GameComponent) -> None:
        if component not in self._gameComponents: raise Exception(f"Cannot remove component {component} before it was added")
        self._gameComponents.remove(component)

