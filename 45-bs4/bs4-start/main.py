from bs4 import BeautifulSoup
import requests 

response = requests.get("https://news.ycombinator.com/news")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

# Get text of all articles
all_a_tags = soup.find_all(class_ = "titleline")

titles = [tag.text for tag in all_a_tags]
links = [tag.find("a")["href"] for tag in all_a_tags]
upvotes = [tag.text for tag in soup.find_all(class_ = "score")]

# Transform upvotes to numeric upvotes 
numeric_upvotes = [int(vote.split()[0]) for vote in upvotes]

largest_votes_index = numeric_upvotes.index(max(numeric_upvotes))

print(titles[largest_votes_index])
print(links[largest_votes_index])
print(numeric_upvotes[largest_votes_index])
































""" with open("website.html") as file:
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

# You can also use css selectors to get tags, but I think I'll skip that part
# Select by class
heading = soup.select(".heading")

 """