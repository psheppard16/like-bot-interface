from tkinter import *
from FrameWork.Screens.screen import Screen
from Imgur import imgur
from imgurpython import ImgurClient
class AccountScreen(Screen):
    def __init__(self, game):
        super().__init__(game, "accountScreen")
        self.clientId = "1a73509dbf251cf"
        self.clientSecret = "3cc02c2a34878b0ce3cd9d81820dc514b34b0f34"
        self.client = ImgurClient(self.clientId, self.clientSecret)

        self.usernameA = StringVar()
        self.usernameAE = Entry(self.game.window.root, width = 40, textvariable=self.usernameA, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold")
        self.usernameAE.pack(in_=self.f, pady=2)
        self.usernameA.set("Account to add")

        self.link = StringVar()

        self.accountAB = Button(self.game.window.root, text="Generate link", command=self.generateLink, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.accountAB.pack(in_=self.f, pady=2)

        self.pin = StringVar()
        pinE = Entry(self.game.window.root, textvariable=self.pin, width=40, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold")
        pinE.pack(in_=self.f, pady=2)
        self.pin.set("Enter pin when prompted")

        self.cancel = Button(self.game.window.root, text="Cancel", command=self.cancel, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.f, pady=2)

        self.listbox = Listbox(self.game.window.root, bg="#%02x%02x%02x" % (255, 165, 0), width=50, font="Helvetica 15 bold")
        self.listbox.pack(in_=self.f, pady=2)

        self.usernameD = StringVar()
        usernameDE = Entry(self.game.window.root, textvariable=self.usernameD, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold")
        usernameDE.pack(in_=self.f, pady=2)
        self.usernameD.set("Account to delete")

        self.accountDB = Button(self.game.window.root, text="Delete account", command=self.delete, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.accountDB.pack(in_=self.f, pady=2)

        self.accept = Button(self.game.window.root, text="Accept", command=self.accept, bg="#%02x%02x%02x" % (0, 255, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.accept.pack(in_=self.f, pady=15)

        self.quitB = Button(self.game.window.root, text="Quit", command=self.quit, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.quitB.pack(in_=self.f, pady=15)

    def generateLink(self):
        self.usernameAE.config(textvariable=self.link)
        self.link.set(self.client.get_auth_url('pin'))
        self.accountAB.config(text="Enter the pin provided by the link", command=self.add)


    def add(self):
        imgur.createAccount(self.usernameA.get(), self.clientId, self.clientSecret, self.client, self.pin.get())
        self.listbox.delete(0, END)
        self.setUp()

    def delete(self):
        imgur.deleteAccount(self.usernameD.get())
        self.listbox.delete(0, END)
        for account in imgur.loadAllAccounts():
            self.listbox.insert(END, "Name: " + account.name + "  |  Username: " + account.accountUsername)

    def quit(self):
        self.game.window.root.destroy()

    def setUp(self):
        self.usernameAE.config(textvariable=self.usernameA)
        self.usernameA.set("Account to add")

        self.accountAB.config(text="Generate link", command=self.generateLink)

        self.pin.set("Enter pin when prompted")

        self.listbox.delete(0, END)
        for account in imgur.loadAllAccounts():
            self.listbox.insert(END, "Name: " + account.name + "  |  Username: " + account.accountUsername)
        self.f.pack(side=LEFT)

    def cancel(self):
        self.setUp()

    def accept(self):
        self.game.saveEngine.saveCharacter(self.game.saveEngine.saveNumber)
        self.game.screenEngine.rMenu = "mainMenu"