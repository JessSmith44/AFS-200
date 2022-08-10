from socket import timeout
from urllib import response
import requests

class Users():
    def __init__(self, firstName, lastName, email, userName, pw, uuid, phone, cell, picLg, picthb, nat):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.uName = userName
        self.pw = pw
        self.uuid = uuid
        self.phone = phone
        self.cell = cell
        self.picLg = picLg
        self.picthb = picthb
        self.nat = nat

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def setemail(self, email):
        self.email = email

    def setuserName(self, userName):
        self.userName = userName

    def setPw(self, pw):
        self.pw = pw

    def setUuid(self, uuid):
        self.uuid = uuid

    def setPhone(self, Phone):
        self.Phone = Phone

    def setCell(self, cell):
        self.cell = cell

    def setPicLg(self, picLg):
        self.picLg = picLg

    def setPicthb(self, picthb):
        self.picthb = picthb

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getemail(self):
        return self.email

    def getuserName(self):
        return self.userName

    def getPw(self):
        return self.pw

    def getUuid(self):
        return self.uuid

    def getPhone(self):
        return self.Phone

    def getCell(self):
        return self.cell

    def getPicLg(self):
        return self.picLg

    def getPicthb(self):
        return self.picthb

    def nationality(self):
        return self.nat

    def __str__(self):
        retStr = self.firstName
        retStr += " "
        retStr += self.lastName
        retStr += " ("
        retStr += self.email
        retStr += ")"

        return retStr

class AuthorizedUsers():
    def __init__(self):
        self.users = []

    def appendUser(self, user):
        self.users.append(user)

    def showUsers(self):
        for user in self.users:
            print(user.__str__())

def getData(userInfo):
    URL = "https://randomuser.me/api/?nat=us"

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON

    except requests.exceptions.HTTPError as errc:
        print(errc)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

myAuthorizedUsers = AuthorizedUsers()

for u in range(0,10):

    jsonUserData = getData("userInfo")

    for currentUser in jsonUserData["results"]:
        firstName = currentUser["name"] ["first"]
        lastName = currentUser["name"] ["last"]
        email = currentUser["email"]
        userName = currentUser["login"] ["username"]
        pw = currentUser["login"] ["password"]
        uuid = currentUser["login"] ["uuid"]
        phone = currentUser["phone"]
        cell = currentUser["cell"]
        picLg = currentUser["picture"] ["large"]
        picthb = currentUser["picture"] ["thumbnail"]
        nat = currentUser["nat"]
        
        newUser = Users(firstName, lastName, email, userName, pw, uuid, phone, cell, picLg, picthb, nat)
        # newUser must pass in all values from users.__init__
        myAuthorizedUsers.appendUser(newUser)

myAuthorizedUsers.showUsers()
