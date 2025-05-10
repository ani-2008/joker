import requests
import sys
url = "https://v2.jokeapi.dev/joke/"

category = ["Programming","Miscellaneous","Dark","Pun","Spooky","Christmas","Any"]

print(category,end=" ")
try:
    choice = int(input(": "))-1
    if 0 <= choice <= 5:
        choice = choice
    else:
        print("Invalid input")
        sys.exit()
    
    url += category[choice]

    response = requests.get(url)
    data = response.json()
    if "setup" in data and "delivery" in data:
        print(data["setup"],data["delivery"],sep="\n")
    else:
        print(data["joke"])
except ValueError:
    print("Invalid input")
