__author__ = 'psheppard16'
import tkinter
class Window:
    def __init__(self, game):
        self.game = game

        self.width = 1280
        self.height = 720

        #setting up the default settings for window
        self.root = tkinter.Tk()
        self.root.title("Red Shooter")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.root.bind_all('<KeyPress>', self.keyPressed)
        self.root.bind_all('<KeyRelease>', self.keyReleased)

    def run(self):
        self.changeWindowSize(self.game.saveEngine.save.resolution)
        self.root.update()

    def changeWindowSize(self, resolution):
        if str(self.width) + 'x' + str(self.height) != self.game.saveEngine.save.resolution:
            self.root.geometry(resolution)
            self.width = self.root.winfo_width()
            self.height = self.root.winfo_height()
            self.game.screenEngine.updateScreens(self.width, self.height)


    def keyPressed(self, event):
        if event.keysym == "Escape":
            self.game.saveEngine.saveCharacter(self.game.saveEngine.saveNumber)
            self.root.destroy()

    def keyReleased(self, event):
        pass