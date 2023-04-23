import requests

from time import sleep

from bs4 import BeautifulSoup
from readability import Document

# Where did I stop, before flying over to Paris
# (need something to listen to)?

next_link = 'https://wanderinginn.com/2017/10/03/3-20-t/'

order = 0

# Trying to be polite with the server.
WAIT_TIME = 10
max_stories = 2

while next_link:
  print(f'Next = [{next_link}]')

  req = requests.get(next_link)
  text = req.text

  soup = BeautifulSoup(text, 'html.parser')
  next_link_elem = soup.find(rel='next')
  next_link = None
  if next_link_elem:
    next_link = next_link_elem['href']

  doc = Document(text)
  soup = BeautifulSoup(doc.summary(), 'html.parser')

  article = soup.text
  # https://stackoverflow.com/a/11566398
  article = article.replace(u'\xa0', u' ')

  title = doc.title()

  if '|' in title:
    title = title.split('|')[0].strip()

  clean_title = "".\
    join([s for s in title if s.isalnum() or s.isspace() or s in ['.']]).\
    replace(' ', '_').\
    lower()

  file_name = f'{order:04d}_{clean_title}'

  with open(f'{file_name}.txt', 'w+') as f:
    f.write(article)

  order = order + 1
  max_stories = max_stories - 1
  if max_stories == 0:
    break

  sleep(WAIT_TIME)
