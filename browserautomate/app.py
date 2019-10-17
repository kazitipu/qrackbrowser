import webbrowser
import random
import time

while True:
    sites=random.choice(['google.com', 'youtube.com', 'boxofficeindia.com', 'boxofficemojo.com'])
    visit='http://{}'.format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)


