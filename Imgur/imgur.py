__author__ = 'Preston Sheppard'
from os import listdir
from os.path import isfile, join
import os
import requests
import pickle
from Imgur.imgurAccount import ImgurAccount
def createAccount(name, clientId, clientSecret, client, pin, extension=False):
    newAccount = None
    if extension:
        filePath = "Imgur/accounts/" + name
    else:
        filePath = "Imgur/accounts/" + name + ".txt"
    try:
        with open(filePath):
            raise Exception("An account with that name already exists")
    except IOError:
        newAccount = ImgurAccount(name, clientId, clientSecret, client, pin)
        open(filePath, "a")
        with open(filePath, 'wb') as input:
            pickle.dump(newAccount, input, pickle.HIGHEST_PROTOCOL)
    if accountIsUnique(newAccount):
        return newAccount
    else:
        deleteAccount(newAccount.name)
        raise Exception("There is already an account registered to that user")

def accountIsUnique(accountToCheck):
    accounts = loadAllAccounts()
    for account in accounts:
        if accountToCheck.name != account.name:
            if accountToCheck.accountUsername == account.accountUsername:
                return False
    return True

def deleteAccount(name, extension=False):
    if extension:
        os.remove("Imgur/accounts/" + name)
    else:
        os.remove("Imgur/accounts/" + name + ".txt")

def loadAccount(name, extension=False):
    if extension:
        filePath = "Imgur/accounts/" + name
    else:
        filePath = "Imgur/accounts/" + name + ".txt"
    try:
        with open(filePath, 'rb') as file:
            return pickle.load(file)
    except IOError:
        raise Exception("An account with that name does not exists")

def deleteAllAccounts():
    accountDir = "accounts"
    accountFiles = [f for f in listdir(accountDir) if isfile(join(accountDir, f))]
    for fileName in accountFiles:
        os.remove(accountDir + "/" + fileName)

def loadAllAccounts():
    accounts = []
    accountDir = "Imgur/accounts"
    accountFiles = [f for f in listdir(accountDir) if isfile(join(accountDir, f))]
    for fileName in accountFiles:
        accounts.append(loadAccount(fileName, extension=True))
    return accounts

def getSubmissions(accessToken, username, page=0):
    endPoint = "https://api.imgur.com/3/account/" + username + "/submissions/" + str(page)

    headers = {'Authorization': 'Bearer ' + accessToken}

    request = requests.get(endPoint, headers=headers)

    return request.json()['data']

def upvoteAllPosts(accessToken, username):
    submissions = getSubmissions(accessToken, username)
    accounts = loadAllAccounts()
    for submission in submissions:
        for account in accounts:
            print("upvoting")
            account.upvotePost(submission['id'])
            print("done!")

def upvoteMostRecentPost(accessToken, username):
    submissions = getSubmissions(accessToken, username)
    accounts = loadAllAccounts()
    for account in accounts:
        account.upvotePost(submissions[0]['id'])