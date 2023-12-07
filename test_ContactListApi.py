import requests
import json
import random

contact_id = {}
bearer_token = ""
user_name = "test712@abc.com"
new_user = "test"+str(random.randint(1,1000))+"@abc.com"

# This function logs into contact list app and returns bearer toke for the user
# The token will be sent in headers of the all subsequent requests
# CRUD
# Add user, add a new contact to the list, get new contact ID
# Update the new contact ID, Delete the newly created contact

def user_login(user_name):
   url = "https://thinking-tester-contact-list.herokuapp.com/users/login"
   payload = json.dumps({
      "email": user_name,
      "password": "Sivaom1$"
   })
   headers = {'Content-Type': 'application/json'}
   response = requests.request("POST", url, headers=headers, data=payload)
   json_response = response.json()
   # print (response.text)
   bearer_token = json_response['token']
   # print(bearer_token)
   return bearer_token


#add New user
def test_addUser_profile():
    url = "https://thinking-tester-contact-list.herokuapp.com/users"
    token = user_login(user_name)

    payload=json.dumps({
    'firstName': 'fkjhjk',
    'lastName': 'fkgjlk',
    'email': new_user,
    'password': 'Sivaom1$'
    })

    headers = {
        'Authorization': 'Bearer '+token,
        'Content-Type': 'application/json'
    }
    print(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 201
    assert response.json()['user']['email'] == new_user

def test_getContacts():
    url = "https://thinking-tester-contact-list.herokuapp.com/contacts"
    token=user_login(new_user)
    payload = {}
    headers = {
        'Authorization': 'Bearer '+token
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print("Contacts List")
    print(response.text)


def test_addContacts():
    url = "https://thinking-tester-contact-list.herokuapp.com/contacts"
    token = user_login(new_user)
    #print(token)

    payload = json.dumps({
        "firstName": "John",
        "lastName": "Doe",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    })
    headers = {
        'Authorization': 'Bearer '+token,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print("New Contact Added: ")
    print(response.text)
    json_response = response.json()
    contact_id["id"] = json_response["_id"]
    assert response.status_code == 201

def test_updateContact():

    url = "https://thinking-tester-contact-list.herokuapp.com/contacts/"+contact_id['id']
    token = user_login(new_user)
    payload = json.dumps({
        "firstName": "Nathan"
    })
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    response = requests.request("PATCH", url, headers=headers, data=payload)
    print("New Contact Updated: ")
    print(response.text)
    assert response.status_code == 200
    assert response.json()['firstName'] == 'Nathan'


def test_deleteContact():
    url = "https://thinking-tester-contact-list.herokuapp.com/contacts/"+contact_id['id']
    token = user_login(new_user)

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert response.text == 'Contact deleted'