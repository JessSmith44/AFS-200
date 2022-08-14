
# Retrieve the data for 25 users located in the "US" from the API "https://randomuser.me/ (Links to an external site.)"
# Store each user in the "Address Book". You will need to create a new instance of the AddressBook class before you can use it.
# You will need to create a new contact for each user from the API before you can store it.
from flask import Flask, request, render_template
import json
from socket import timeout
from urllib import response
from addressbook import AddressBook, Contact
# import addressbook
import requests

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


theAddressBook = AddressBook()

for u in range(0,25):    

    jsonUserData = getData("userInfo")

    for currentUser in jsonUserData["results"]:
        firstName = currentUser["name"] ["first"]
        lastName = currentUser["name"] ["last"]
        email = currentUser["email"]
        phone = currentUser["phone"]
        photo = currentUser["picture"] ["large"]
        nat = currentUser["nat"]

        newContact = Contact(firstName, lastName, email, phone, photo)
        # print(newContact) 25 contacts print as they should.
        theAddressBook.addAddress(newContact)

    # print(jsonUserData)
    # print is getting data
theAddressBook.getAllAddresses()
# print(theAddressBook)

app = Flask(__name__)

# Create routes to handle the following URLs.  These routes should render the "index.html" file in the templates directory.
# http://127.0.0.1:5000/ (Method is GET)
# Display all of the entries in our address book.

@app.route("/")
def home():
    contactsResults = theAddressBook.getAllAddresses()
    return render_template('index.html', results = contactsResults)
    # testingtestingtestingtestingtesting
# http://127.0.0.1:5000/search (Method is POST)
# Retrieve the search value from the request object
# Find all matching entries in our address book that match
# Display the results to the user.

@app.route("/search", methods=['POST'])
def getContact():
    if request.method == 'POST':
        inputValue = request.form.get('search')
        results = theAddressBook.findAllMatching(inputValue)
        return render_template('index.html', results = results)
    else:
        return "Oh no! Looks like that contact does not exsist."    
       
if __name__ == "__main__":
    app.run()