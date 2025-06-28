import json
import requests as rs

url = "http://216.10.245.166/Library/GetBook.php"
resp = rs.get(url,params={"AuthorName": "Rahul Shetty"},)
print("Response Type:", type(resp))
rs_text = resp.text
print("Response text type:",type(rs_text))
print("Response Text:",rs_text)
print("Status Code:",resp.status_code)

assert resp.status_code == 200, "Status code is not 200"
print("--Successfully validated the status code--")
print("Response Content:",resp.content)
print("Response Headers:",resp.headers)
print("Content-Type Header:", resp.headers["Content-Type"])
assert resp.headers["Content-Type"] == "application/json;charset=UTF-8", "Content-Type is not as expected"
print("--Successfully validated the Content-Type header--")
json_response = resp.json()
print("JSON Response Type:", type(json_response))
print("First Book ISBN:", json_response[0]["isbn"])
print("First Book Name:", json_response[0]["book_name"])

import pytest
@pytest.mark.parametrize("author_name, expected_isbn", [
    ("Rahul Shetty", "A1b"),
    ("John Doe", "XYZ123")  # Example for another author
])
def test_get_book_by_author(author_name, expected_isbn):
    response = rs.get(url, params={"AuthorName": author_name})
    assert response.status_code == 200, f"Failed to get books for {author_name}"
    json_response = response.json()
    assert len(json_response) > 0, f"No books found for {author_name}"
    assert json_response[0]["isbn"] == expected_isbn, f"Expected ISBN {expected_isbn} but got {json_response[0]['isbn']}"
    print(f"Test passed for author: {author_name} with ISBN: {expected_isbn}")

