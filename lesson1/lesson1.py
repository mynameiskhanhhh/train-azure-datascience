from bs4 import BeautifulSoup
import requests

website = "https://subslikescript.com/movie/The_Breach-14229154"
results = requests.get(website)
content = results.text

# Get title & transcript
soup = BeautifulSoup(content, "lxml")

box = soup.find("article", class_ = "main-article")
title = box.find("h1").get_text()
# print(title)

script_raw = box.find("div", class_ = "full-script")
for br in script_raw.select("br"):
    br.replace_with("\n")
script = script_raw.get_text()
# print(script)

with open(f"{title}.txt", "w", encoding = "utf-8") as f:
    f.write(title + "\n")
    f.write(script)
    f.close()
