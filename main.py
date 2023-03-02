import requests
from tinydb import TinyDB, Query
param={
    'results':5
}
response = requests.get("https://randomuser.me/api/",params=param)
data = response.json()["results"][0]
print(data)

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
    "age": age, 
    "phone": phone, 
    "country": country, 
    "email": email}
db.insert(user)