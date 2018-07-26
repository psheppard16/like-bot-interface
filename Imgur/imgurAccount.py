__author__ = 'Preston Sheppard'
import requests
import pickle
from pprint import pprint
class ImgurAccount():
    def __init__(self, name, clientId, clientSecret, client, pin):
        self.name = name
        self.clientId = clientId
        self.clientSecret = clientSecret

        self.accountUsername = None
        self.accountId = None
        self.refreshToken = None

        credentials = client.authorize(pin, 'pin')
        self.refreshToken = credentials['refresh_token']
        self.accountUsername = credentials['account_username']
        self.accountId = credentials['account_id']

    def getAccessToken(self):
        endPoint = "https://api.imgur.com/oauth2/token"

        data = {'refresh_token': self.refreshToken,
                'client_id': self.clientId,
                'client_secret': self.clientSecret,
                'grant_type': "refresh_token"}

        request = requests.post(endPoint, data=data)
        accessToken = request.json()['access_token']
        return accessToken

    def saveAccount(self):
        filePath = "accounts/" + self.name + ".txt"
        open(filePath, "a") #checks if file exists, if it doesn't, creates it
        try:
            with open(filePath, 'wb') as output:
                pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
        except EOFError and FileNotFoundError:
            raise Exception("File not found")

    def upvotePost(self, postId):
        endPoint = "https://api.imgur.com/3/gallery/" + postId + "/vote/up"

        headers = {'Authorization': 'Bearer ' + self.getAccessToken()}

        request = requests.post(endPoint, headers=headers)

        if request.json()['success'] == True:
            print("upvoting successful")
        else:
            pprint(request.json())
            print("upvoting failed")

    def uploadImage(self, image, name, title, description):
        endPoint = "https://api.imgur.com/3/image"

        imageData = {'description': description,
                     'name': name,
                     'title': title,
                     'image': image}

        headers = {'Authorization': 'Bearer ' + self.getAccessToken()}

        request = requests.post(endPoint, data=imageData, headers=headers)
        r = request.json()
        return r['data']['id'], r['data']['title']

    def shareImage(self, imageId, imageTitle):
        endPoint = "https://api.imgur.com/3/gallery/image/" + imageId

        headers = {'Authorization': 'Bearer ' + self.getAccessToken()}

        postData = {'title': imageTitle}

        request = requests.post(endPoint, data=postData, headers=headers)

        pprint(request.json())

    def uploadAndShare(self, image, name, title, description):
        imageId, imageTitle = self.uploadImage(image, name, title, description)
        self.shareImage(imageId, imageTitle)

    def getSubmissions(self, page=0):
        endPoint = "https://api.imgur.com/3/account/" + self.accountUsername + "/submissions/" + str(page)

        headers = {'Authorization': 'Bearer ' + self.getAccessToken()}

        request = requests.get(endPoint, headers=headers)

        return request.json()['data']

