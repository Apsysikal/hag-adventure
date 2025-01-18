from selection import Selection


print("Welcome to the Hansle and Gretle Adventure!")
selector = Selection(["load", "New Game"],"Do you want to load a game or start a new one?")
selectetOption = selector.serve()

print(selectetOption)


selector = Selection(["load", "New Game", {"menu" ,["load", "save", "exit"]}])
