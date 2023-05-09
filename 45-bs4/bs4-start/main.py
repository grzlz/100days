from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# Get all p tags
all_p_tags = soup.find_all(name = "p")
# print(all_p_tags)
# Returns a list containing all the p tags

# Get text on all p tags
all_p_text = [p.text for p in all_p_tags]
# print(all_p_text)

# Get all hrefs (links) from anchor tags
all_a_tags = soup.find_all(name = "a")
all_links = [a_tag.get("href") for a_tag in all_a_tags]
# print(all_links)

# Find tags by class 
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)




