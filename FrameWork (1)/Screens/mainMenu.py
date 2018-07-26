__author__ = 'psheppard16'
from tkinter import *
from FrameWork.Screens.screen import Screen
from Imgur import imgur
class MainMenu(Screen):
    def __init__(self, game):
        super().__init__(game, "mainMenu")
        self.clientId = "b41989483eb0563"
        self.clientSecret = "2547ea796fa5c2e9b7e964e7f747ef013f90d9dc"

        self.startB = Button(self.game.window.root, text="Run", command=self.run, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.startB.pack(in_=self.f, pady=15)

        self.account = Button(self.game.window.root, text="Manage Accounts", command=self.account, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.account.pack(in_=self.f, pady=15)

        self.optionsB = Button(self.game.window.root, text="Options", command=self.options, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.optionsB.pack(in_=self.f, pady=15)

        self.instructionsB = Button(self.game.window.root, text="Instructions", command=self.instructions, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.instructionsB.pack(in_=self.f, pady=15)

        self.quitB = Button(self.game.window.root, text="Quit", command=self.quit, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.quitB.pack(in_=self.f, pady=15)

    def quit(self):
        self.game.window.root.destroy()

    def options(self):
        self.game.screenEngine.rMenu = "options"

    def account(self):
        self.game.screenEngine.rMenu = "accountScreen"

    def run(self):
        accounts = imgur.loadAllAccounts()
        for account in accounts:
            if self.game.saveEngine.save.allPosts:
                imgur.upvoteAllPosts(account.getAccessToken(), self.game.saveEngine.save.usernameToLike)
            else:
                imgur.upvoteMostRecentPost(account.getAccessToken(), self.game.saveEngine.save.usernameToLike)
        print("done upvoting")

    def instructions(self):
        self.game.screenEngine.rMenu = "instructions"