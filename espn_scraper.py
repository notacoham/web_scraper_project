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

# 