import json
import configparser
from payLoad import *
from utilities.resources import *
from utilities.configurations import *

import requests

# --------- Post
url = getConfig()["API"]["endpoint"] + ApiResources.addBook
print("URL:", url)  # op:URL: http://216.10.245.166/Library/Addbook.php
headers = {"Content-Type": "application/json"}
addBook_response = requests.post(
    url,
    json=addBookPayload("fefrewe"),
    headers=headers,
)

print(addBook_response.json())  # {'Msg': 'successfully added', 'ID': 'fefrewe227'}
response_json = addBook_response.json()
print("Json type:", type(response_json))  # Json type: <class 'dict'>

bookId = response_json["ID"]
print("Book ID:", bookId)  # Book ID: fefrewe227

# -------- Delete Book
response_deleteBook = requests.post(
    "http://216.10.245.166/Library/DeleteBook.php",
    json={"ID": bookId},
    headers={"Content-Type": "application/json"},
)

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print("Json Response:", res_json["msg"])  # Json Response: book is successfully deleted
assert res_json["msg"] == "book is successfully deleted"

# ----------- Authentication
url = "https://api.github.com/user"
github_response = requests.get(
    url, verify=False, auth=("rahulshettcademy", getPassword())
)

print("Git Hub Status Code:", github_response.status_code)  # Git Hub Status Code: 401
