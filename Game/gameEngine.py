from Game.GameObjects.square import Square
class GameEngine:
    def __init__(self, game):
        self.game = game
        self.square = Square(game)

    def run(self):
        print("running")

    def keyReleased(self, event):
        if event.keysym == "a":
            print("a key pressed")


    def keyPressed(self, event):
        if event.keysym == "a":
            print("a key released")





