import requests
from tinydb import TinyDB, Query

def random_user(n):
    db = TinyDB('randomuser.json', indent=4)
    param = {'results': n}
    response = requests.get("https://randomuser.me/api/", params=param)
    data = response.json()["results"]
    for user_data in data:
        first_name = user_data["name"]["first"]
        last_name = user_data["name"]["last"]
        age = user_data["dob"]["age"]
        phone = user_data["phone"]
        country = user_data["location"]["country"]
        email = user_data["email"]

        user = {
            "first_name": first_name, 
            "last_name": last_name, 
            "age": age, 
            "phone": phone, 
            "country": country, 
            "email": email
        }
        db.insert(user)

random_user(100)