import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')


# This function sort the stories by their votes.
def sort_stories_by_votes(news_list):
    return sorted(news_list, key = lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hacker_news = []

    for idx, item in enumerate(links):
        title = item.getText()
        # Select the first anchor tag
        link_tag = item.select_one('a')
        # Get the href attribute from the anchor tag
        href = link_tag['href'] if link_tag else 'None'
        # Get the votes
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hacker_news.append({'title:': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hacker_news)

pprint.pprint(create_custom_hn(links, subtext))