
import dota2api
import csv
import json

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

	# results = api.get_match_history()

	# print "Number of matches ", len(results["matches"])
	# print "results remaining ", results["results_remaining"]

	# results = api.get_match_history()

	# print "Number of matches ", len(results["matches"])
	# print "results remaining ", results["results_remaining"]

	# results = api.get_match_history()

	# print "Number of matches ", len(results["matches"])
	# print "results remaining ", results["results_remaining"]


if __name__ == "__main__":
	get_matches()
	






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