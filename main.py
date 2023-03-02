import requests
from tinydb import TinyDB, Query

response = requests.get("https://randomuser.me/api/")
data = response.json()["results"][0]


first_name = data["name"]["first"]
last_name = data["name"]["last"]
age = data["dob"]["age"]
phone = data["phone"]
country = data["location"]["country"]
email = data["email"]

db = TinyDB('randomuser.json')
user = {
    "first_name": first_name, 
    "last_name": last_name, 
    "age": age, "phone": phone, 
    "country": country, 
    "email": email}
db.insert(user)

User = Query()
result = db.search(User.first_name == first_name)

print(result)