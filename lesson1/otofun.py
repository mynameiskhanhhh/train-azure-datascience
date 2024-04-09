from bs4 import BeautifulSoup
import requests
import os

def output_file(file_name):
    directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, file_name)
    with open(f"{file_path}.txt", "w", encoding = "utf-8") as f:
        f.write(title + "\n\n")
        f.write("Username: " + username[:username.index(" ")] + "\n")
        f.write("Name: " + user + "\n")
        f.write(message)
        f.close()

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

output_file(title)