import email
import requests

class Contact():
    
    def __init__(self, firstName, lastName, email, phone, photo):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.photo = photo

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone 

    def getPhoto(self):
        return self.photo

# Define two additional methods called "__str__" and "__repr__".  Both of these methods should return a string value of the object.  
# Suggestion would be name and email address.  For example:  John Smith (jsmith@gmail.com)

    def __str__(self):
        retStr = self.photo
        retStr += " "
        retStr += self.firstName
        retStr += " "
        retStr += self.lastName
        retStr += " "
        retStr += self.email
        retStr += " "
        retStr += self.phone

        return retStr

    def __repr__(self):
        return self.firstName

class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        # print(address)
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)
                
        return results
    
# make basic flask server