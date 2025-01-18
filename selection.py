import inquirer
from typing import List

class Selection:
    def __init__(self, options: List[str] = [] , question = "What do you do?"):
        self.collection = options
        self.question = question


    def add(self, option: str):
        self.collection.append(option)
        return self

    def serve(self) -> str:
        answer = inquirer.prompt([
            inquirer.List('options',
                    message=self.question,
                    choices=self.collection)
        ])["options"]

        self.collection = []
        return answer

    