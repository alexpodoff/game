
from game.menu import Menu
from game.base import Construct


menu = Menu()
menu.start()


draft_player = Construct(menu.race, menu.gender, menu.name)
player = draft_player.player_build()
print(player)

