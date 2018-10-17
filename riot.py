#from riotwatcher import RiotWatcher
import requests
"""
watcher = RiotWatcher()
region = 'na1'

me = watcher.summoner.by_name(region, 'napavementape')
print(me)
"""


def get_data():
	return requests.get('https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/30663153?api_key=')

def store(x):
	f = open('data.txt', 'r+')
	f.writelines(list(x.text))
	for line in f:
		print (line)

r = get_data()
store(r)
