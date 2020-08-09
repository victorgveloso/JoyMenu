import joymenu.game
import joymenu.menuentries

g = joymenu.game.Game(joymenu.menuentries.Parser().entries)
g.main_loop()
