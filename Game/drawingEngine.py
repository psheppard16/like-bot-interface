__author__ = 'python'
from FrameWork.Display.canvasObject import CanvasObject
try:
    import pygame
except:
    pass
class DrawingEngine(CanvasObject):
    def __init__(self, game):
        #Drawing engine is a child of CanvasObject,
        #which contains the drawing methods for canvas
        super().__init__(game)

        self.game = game
        self.gameEngine = game.gameEngine #providing access to gameEngine


    def getScreenX(self, x):
        """
        This function is used by all the draw methods. By default, it does nothing.
        When a draw method is passed, "shiftPosition=True", which is false by default,
        all x coordinates passed to that function will be passed through this function,
        and then the return value will be used to display the object.
        This allows for easy and convenient shifts and scales to be used often without
        cluttering display code.
        :param x: the x location of the object
        :return: the x location of the object on the screen
        """
        return x

    def getScreenY(self, y):
        """
        This function is used by all the draw methods. By default, it makes the 0,0 of the
        display be in the bottom left of the screen instead of the upper right.
        When a draw method is passed, "shiftPosition=True", which is false by default,
        all y coordinates passed to that function will be passed through this function,
        and then the return value will be used to display the object.
        This allows for easy and convenient shifts and scales to be used often without
        cluttering display code.
        :param y: the y location of the object
        :return: the y location of the object on the screen
        """
        return self.game.window.height - y

    def draw(self):
        """
        This method is called every tick. All draw methods should be called here.

        For a complete list of draw function go to FrameWork --> Display --> canvasObject
        To change the background color: self.game.canvasObject.backgroundColor =
        :return: None
        """

        #draw method examples:
        self.showRectangle((100, 100), (200, 200), (255, 0, 165), secondaryColor=(255, 255 ,0), width=2, shiftPosition=True)
        self.showRectangle((100, 100), (200, 200), (255, 0, 0))
        self.showCircle((500, 500), 100, (255, 165, 0))


