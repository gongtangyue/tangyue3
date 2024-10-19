from bs4 import BeautifulSoup
import requests

url = "https://www.homes.com/texas/homes-for-rent/?bb=9-ggv1rgtLo33z4kstD"
response = requests.get(url)

doc = BeautifulSoup(response.text, 'html.parser')

#with open("texas_rent_price.html", "r") as f:
#    doc = BeautifulSoup(f, "html.parser")

house = doc.find_all("li", class_="placard-container")
print(len(house))