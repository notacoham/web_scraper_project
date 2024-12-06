from bs4 import BeautifulSoup
import requests
import smtplib

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

# initialize the final arrays
stories_names = []
stories_dates = []
stories_content = []

# loop over stories array
for story in stories:
    story_name = story.a.text
    story_date = story.find('span', class_='short').text.replace('\n', '').replace('  ', '').replace('\xa0', '').replace('|', '')
    story_content = story.h5.text
    stories_names.append(story_name)
    stories_dates.append(story_date)
    stories_content.append(story_content)
    
# Email functionality

email = 'alexcottam12@gmail.com'
receiver_email = 'alexcottam12@gmail.com'

subject = f'UHC Top Stories for Today {top_story_header}'
message = f'{top_story_header}\n{top_story_subheader}\n----------\n1. {stories_names[0]}\n2. {stories_names[1]}\n3. {stories_names[2]}\n4. {stories_names[3]}\n5. {stories_names[4]}\n'
link = f'To read the full stories go to {url}'

text = f'Subject: {subject}\n\n{message}\n\n{link}'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(email, 'uprr kjsp rciw qafc')

server.sendmail(email, receiver_email, text)

print('Email has been sent to: ' + receiver_email)