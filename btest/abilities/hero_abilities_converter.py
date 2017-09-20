import json
from collections import OrderedDict


with open('hero_abilities.json') as filepath:
 	hero_abilities = json.load(filepath, object_pairs_hook=OrderedDict)



for key, val in hero_abilities.iteritems():
	for i in range(len(val["abilities"])):
		hero_abilities[key]["abilities"][i] = [val["abilities"][i], 1]

with open('my_hero_abilities.json', 'wb') as filepath:
        json.dump(hero_abilities, filepath, indent=4, sort_keys=False)