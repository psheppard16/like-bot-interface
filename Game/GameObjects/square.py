from Game.GameObjects.gameObject import GameObject
class Square(GameObject):
    def __init__(self, game):
        super().__init__(game, 500, 500, xVel=5, layer=100)
        self.size = 100
        pass

    def draw(self, drawingEngine):
        drawingEngine.showRectangle((self.x - self.size / 2, self.y - self.size / 2),
                                    (self.x + self.size / 2, self.y + self.size / 2), (255, 0, 0))

    def run(self, gameEngine):
        self.move()