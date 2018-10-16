#from riotwatcher import RiotWatcher
import requests
"""
watcher = RiotWatcher('RGAPI-51de6acf-ddb3-402b-82ea-cd61e272880a')
region = 'na1'

me = watcher.summoner.by_name(region, 'napavementape')
print(me)
"""


def get_data():
	return requests.get('https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/30663153?api_key=RGAPI-51de6acf-ddb3-402b-82ea-cd61e272880a')

def store(x):
	f = open('data.txt', 'r+')
	f.writelines(list(x.text))
	for line in f:
		print (line)

r = get_data()
store(r)