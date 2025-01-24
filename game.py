from Framework.Game import Game
from Framework.GameComponent import GameComponent

class AdventureGame(Game):

    def __init__(self):
        super().__init__()

    def initialize(self):
        return super().initialize()
    
    def update(self):
        return super().update()
    

class TestComponent(GameComponent):
    
    def __init__(self):
        super().__init__()

    def initialize(self):
        super().initialize()
        print(f"Initializing component: {self}")

    def update(self):
        super().update()
        print(f"Updating component: {self}")


if __name__ == "__main__":
    game = AdventureGame()
    components = [
        TestComponent(),
        TestComponent(),
        TestComponent()
    ]

    for component in components:
        game.addComponent(component)

    

        
    game.initialize()
    for i in range(5):
        game.update()