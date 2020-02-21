from bs4 import BeautifulSoup
import requests

handle = input('Input your account name on Twitter: ')
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text, 'lxml')

try:
    follow_box = bs.find(
        'li', {'class': 'ProfileNav-item ProfileNav-item--followers'})
    followers = follow_box.find('a').find(
        'span', {'class': 'ProfileNav-value'})
    print("Number of followers: {} ".format(followers.get('data-count')))

    following_box = bs.find(
        'li', {'class': 'ProfileNav-item ProfileNav-item--following'})
    following = following_box.find('a').find(
        'span', {'class': 'ProfileNav-value'})
    print("{} is following {} people.".format(
        handle, following.get('data-count')))

    favorite_box = bs.find(
        'li', {'class': 'ProfileNav-item ProfileNav-item--favorites'})
    favorite = favorite_box.find('a').find(
        'span', {'class': 'ProfileNav-value'})
    print("Number of post {}  liked are {}: ".format(
        handle, favorite.get('data-count')))

    tweet_box = bs.find(
        'li', {'class': 'ProfileNav-item ProfileNav-item--tweets is-active'})
    tweets = tweet_box.find('a').find('span', {'class': 'ProfileNav-value'})
    print("{} has tweeted {} tweets.".format(
        handle, tweets.get('data-count')))


except:
    print('Account name not found...')

