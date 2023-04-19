from bs4 import BeautifulSoup

with open("website.html") as file: 
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.ul)

all_anchor_tags = soup.find_all("a")

for tag in all_anchor_tags:
    print(tag.getText())