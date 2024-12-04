from bs4 import BeautifulSoup
import requests

# URL assignment
url = 'https://www.ksl.com/sports/utah-hockey-club'

# assign scraped data to variables and format
# page
page_content = requests.get(url).text
soup = BeautifulSoup(page_content, 'lxml')

# top story
top_story = soup.find('div', class_='top_story')
top_story_header = top_story.find('h1').text.replace('  ', '')
top_story_subheader = top_story.find('h2').text.replace('  ', '')

# find all stories on main page
stories = soup.find_all('div', class_='headline')

# print top header
print(f'Top Story: {top_story_header}\n--------\n-->{top_story_subheader}\n')

# print all stories
for story in stories:
    story_name = story.a.text
    story_date = story.find('span', class_='short').text.replace('|', '')
    story_content = story.h5.text
    print(f'{story_name}\n->{story_date}\n-->{story_content}\n')
