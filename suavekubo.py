import requests, time, random
import pyperclip
from bs4 import BeautifulSoup as soup

boards = ['a','c','w','m','cgl','cm','n','jp','vp','v','vg','vr','co','g','tv','k','o','an','tg','sp','asp','sci','int','out','toy','biz','i','po','p','ck','ic','wg','mu','fa','3','gd','diy','wsg','s','hc','hm','h','e','u','d','y','t','hr','gif','trv','fit','x','lit','adv','lgbt','mlp','b','r','r9k','pol','soc','s4s']
cache  = {cache: '' for cache in boards}

bannedboards = ['s','hx','hm','h','e','u','d','y','t','hr','gif','b','aco','r']

def init(boardname):
    
    board = boardname
    if board in bannedboards:
        return ['https://i.ytimg.com/vi/WKHTaKdAuEw/hqdefault.jpg','hqdefault.jpg']
    #Request board catalog, and get get a list of threads on the board; then sleeping for 1.5 seconds
    threadnums = list()
    data = ''

    #If a board's catalog has already been requested, just use that stored data instead
    if (cache[board] != ''):
        data = cache[board]
    #else request the catalog, and sleep for 1.5 seconds; storing that data for future use
    else:
        data = (requests.get('http://a.4cdn.org/' + board + '/catalog.json')).json()
        cache[board] = data

    #Get a list of threads in the data
    for page in data:
        for thread in page["threads"]:
            threadnums.append(thread['no'])

    #Select a thread
    thread = random.choice(threadnums)

    #Request the thread information, and get a list of images in that thread; again sleeping for 1.5 seconds
    imgs = list()
    pd = (requests.get('http://a.4cdn.org/' + board + '/thread/' + str(thread) + '.json')).json()
    for post in pd['posts']:
        #Ignore key missing error on posts with no image
        try:
            imgs.append(str(post['tim']) + str(post['ext']))
        except:
            pass

    #Select an image
    image = random.choice(imgs)

    #Assemble and return the urls
    imageurl = 'https://i.4cdn.org/' + board + '/' + image
    thread = 'https://boards.4chan.org/' + board + '/thread/' + str(thread)
    print([ imageurl , image ])
    return [imageurl, image]

def main():
    init('c')

if __name__ == '__main__':
    main()
