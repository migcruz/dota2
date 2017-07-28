# https://homes.cs.washington.edu/~suinlee/genome560/lecture7.pdf
# http://cba.ualr.edu/smartstat/topics/anova/example.pdf
# http://stattrek.com/statistics/notation.aspx
# https://www.qualtrics.com/blog/determining-sample-size/
# http://www.sjsu.edu/faculty/gerstman/StatPrimer/z-two-tails.pdf
# https://stackoverflow.com/questions/20864847/probability-to-z-score-and-vice-versa-in-python
# tableau vs bokeh vs matplotlib for visualization
import dota2api
import csv
import json
import urllib		

import numpy as numpy
import scipy.stats as st

api_key = "A2015A0A612683AC2A8949495104B731"

def api_init():
	api = dota2api.Initialise(api_key)

	return api

def get_write_heroes():
	api = api_init()
	heroes = api.get_heroes()
	heroes_list = heroes['heroes']

	with open('heroes_list.json', 'wb') as filepath:
 		json.dump(heroes_list, filepath)

 	hero_dict = {}
 	for hero in heroes_list:
 		hero_dict[hero["id"]] = hero["localized_name"]

 	with open('hero_id_names.json', 'wb') as filepath:
 		json.dump(hero_dict, filepath)

def get_write_items():

	api = api_init()
	items = api.get_game_items()
	items_list = items['items']

	with open('items_list.json', 'wb') as filepath:
 		json.dump(items_list, filepath)

 	item_dict = {}
 	for item in items_list:
 		item_dict[item["id"]] = item["localized_name"]

 	with open('item_id_names.json', 'wb') as filepath:
 		json.dump(item_dict, filepath)

def get_matches():
	api = api_init()
	results = api.get_match_history(matches_requested=400)

	print "Number of matches ", len(results["matches"])
	print "results remaining ", results["results_remaining"]

	for match in results["matches"]:
		print "ID: ", match['match_id'], ", SEQ#: ", match['match_seq_num']
	# results = api.get_match_history()

	# print "Number of matches ", len(results["matches"])
	# print "results remaining ", results["results_remaining"]

	# results = api.get_match_history()

	# print "Number of matches ", len(results["matches"])
	# print "results remaining ", results["results_remaining"]

	# results = api.get_match_history()

	# print "Number of matches ", len(results["matches"])
	# print "results remaining ", results["results_remaining"]

def get_matches_seq():
	api = api_init()
	results = api.get_match_history_by_seq_num(matches_requested=400)

	print "Number of matches ", len(results["matches"])

	for match in results["matches"]:
		print "ID: ", match['match_id'], ", SEQ#: ", match['match_seq_num']

def opendota_get_matches(match_id=None):

	# Gets a random samle of recent 100 dota 2 matches

	if match_id is None:
		url = "https://api.opendota.com/api/publicMatches"
	else:
		url = "https://api.opendota.com/api/publicMatches?less_than_match_id=" + str(match_id)

	print url
	response = urllib.urlopen(url)
	matches_list = json.loads(response.read())

	return matches_list


def find_lowest(array, param=None):

	quicksort(array, 0, len(array) - 1, key=param)

	for item in array:
		if param is None:
			print item
		else:
	 		print item[param]
	
	if param is None:
		return array[0]
	else:
		return array[0][param]


def quicksort(array, left, right, key=None):

	if (left >= right):
		return

	if key is None:
		pivot = array[(left + right)/2]
	else:
		pivot = array[(left + right)/2][key]


	index = partition(array, left, right, pivot, key);

	quicksort(array, left, index - 1, key);
	quicksort(array, index, right, key);

def partition(array, left, right, pivot, key=None):

	if key is None:

		while (left <= right):

			while (array[left] < pivot):
				left += 1
			while (array[right] > pivot):
				right -= 1

			if (left <= right):
				temp = array[left]
				array[left] = array[right]
				array[right] = temp
				left += 1
				right -= 1
	else:

		while (left <= right):

			while (array[left][key] < pivot):
				left += 1
			while (array[right][key] > pivot):
				right -= 1

			if (left <= right):
				temp = array[left]
				array[left] = array[right]
				array[right] = temp
				left += 1
				right -= 1

	return left


def bucket_sort_mmr(matches_list):

	N = len(matches_list)

	brackets = [[] for i in range(0,6)] # a list of lists 0-5k
	for match in matches_list:
		index = int((match['avg_mmr']/1000))
		if index > 5:
			index = 5
		brackets[index].append(match['match_id'])

	print "After bucket sorting 0-5k"

	for bracket in brackets:
		print len(bracket)


def find_lowest_mmr_match(matches_list):

	quicksort(matches_list, 0, len(matches_list) - 1, key='avg_mmr')

	for match in matches_list:
		print match['avg_mmr']

	return matches_list[0]['avg_mmr']


if __name__ == "__main__":

	matches_list = opendota_get_matches()
	bucket_sort_mmr(matches_list)
	# matchid = find_lowest(matches_list, param='match_id')

	# print "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"

	# matches_list2 = opendota_get_matches(match_id=matchid)
	# matchid = find_lowest(matches_list2, param='match_id')






# # Get stuff
# api = dota2api.Initialise(api_key)

# match = api.get_match_details(match_id=1000193456)

# heroes = api.get_heroes()
# heroes_list = heroes['heroes']

# for key, val in match.iteritems():
# 	print key, val
	#print match

# print "HUMAN PLAYERS: ", match['human_players']
# print match['game_mode']
# print heroes


# # output heroes to a CSV file
# w = csv.writer(open("output.csv", "w"))
# for hero in heroes_list:
# 	for key, val in hero.iteritems():
# 		w.writerow([key, val])


# # read CSV file
# hero_ids = []
# hero_names = []
# for key, val in csv.reader(open("output.csv")):
# 	if key == "id":
# 		hero_ids.append(val)
# 	elif key == "localized_name":
# 		hero_names.append(val)

# hero_dict = {}
# for key, val in zip(hero_ids, hero_names):
# 	hero_dict[key] = val

# # write hero names and ids to json
# with open('hero_id_names.json', 'wb') as filepath:
# 	json.dump(hero_dict, filepath)




# # read heroids and names from json
# with open('hero_id_names.json', 'rb') as filepath:
# 	hero_dict = json.load(filepath)

# hero_dict_inv = {val: key for key, val in hero_dict.iteritems()}

# print hero_dict["5"]
# print hero_dict_inv["Crystal Maiden"]