from bs4 import BeautifulSoup
import requests

website = "https://www.otofun.net/threads/bao-tri-va-nang-cap-trang-choxeotofun-net.1867324/"
content = requests.get(website).text

soup = BeautifulSoup(content, "lxml")

title = soup.find("div", class_ = "p-body").find("h1", class_ = "p-title-value").get_text()
# print(title)

time = soup.find("div", class_ = "message-attribution-main").find("a", class_ = "u-concealed").get_text()
# print(time.strip())

username = soup.find("div", class_ = "message-userDetails").find("span", class_ = "username--style3 username--moderator username--admin").get_text(separator=" ")
user = soup.find("div", class_ = "message-userDetails").find("h5", class_ = "userTitle message-userTitle").get_text()
# print(username[:username.index(" ")].strip())
# print(user.strip())

message = soup.find("article", class_ = "message-body js-selectToQuote").get_text()
# print(message)

with open(f"{title}.txt", "w", encoding = "utf-8") as f:
    f.write(title + "\n\n")
    f.write("Username: " + username + "\n")
    f.write("Name: " + user + "\n")
    f.write(message)
    f.close()