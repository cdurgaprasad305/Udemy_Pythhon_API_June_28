import requests
import json

response = requests.get(
    "http://216.10.245.166/Library/GetBook.php",
    params={"AuthorName": "Rahul Shetty"},
)
"""'
Line-by-Line Explanation
import requests
This imports the requests library, which is used in Python to send HTTP requests (like GET, POST, etc.) to web servers.

import json
Imports the json library, which allows for working with JSON data (parsing, creating, etc.).

response = requests.get(...)
This line sends an HTTP GET request to the URL:
http://216.10.245.166/Library/GetBook.php
It also passes a query parameter:

AuthorName is set to "Rahul Shetty"
So, the final URL looks like:
http://216.10.245.166/Library/GetBook.php?AuthorName=Rahul+Shetty
The response object contains the server’s reply, including data and status code.
"""

print(response.text)
"""
 OP: [{"book_name":"Postman Course","isbn":"A1b","aisle":"1"},
{"book_name":"Learn Appium Automation with Java","isbn":"KM201","aisle":"227"},
{"book_name":"Postman Testing","isbn":"JH642","aisle":"1234"},
{"book_name":"Postman Testing","isbn":"JH876","aisle":"1234"},
{"book_name":"Learn Appium Automation with Java","isbn":"RS49","aisle":"269"},
{"book_name":"Learn Appium Automation with Java","isbn":"RS975","aisle":"269"}]
"""
print(type(response.text))  # OP: <class 'str'>

dict_response = json.loads(response.text)
print(type(dict_response))  # <class 'list'>
print(dict_response[0]["isbn"])  # OP: A1b
print(dict_response[0]["book_name"])  # Postman Course

# ----------------------------------------------------------------------------------
json_response = response.json()
# response.json() converts the JSON data from the response body into a Python
# object (usually a list or dictionary).

print(type(json_response))
print(json_response[0]["isbn"])

assert response.status_code == 200
print(response.headers)
assert response.headers["Content-Type"] == "application/json;charset=UTF-8"

# Retrieve the book details with ISBN RGHCC
actualBook = ""
for actualBook in json_response:
    if actualBook["isbn"] == "RGHCC":
        print(actualBook)
        break

expectedBook = {
    "book_name": "Learn API Automation with RestAssured",
    "isbn": "RGHCC",
    "aisle": "12239",
}

assert actualBook == expectedBook

"""
If actualBook and expectedBook are the same (key-value pairs exactly match), 
the assertion passes and the program continues.

If they do not match, an AssertionError will be raised, indicating either the 
API response is not as expected or there is a mistake in the test.
"""
