import json
from collections import OrderedDict

key_list = []
key_list2 = []

hero_ability = OrderedDict()
hero_npc_id = {}

with open('abilities.json') as filepath:
 	abilities = json.load(filepath, object_pairs_hook=OrderedDict)

with open('hero_abilities.json') as filepath:
 	hero_abilities = json.load(filepath, object_pairs_hook=OrderedDict)

with open('heroes2.json') as filepath:
 	heroes2 = json.load(filepath, object_pairs_hook=OrderedDict)

# Match hero npc name
for key, val in heroes2.iteritems():
	for key2, val2 in hero_abilities.iteritems():
		if key2 == val["name"]:
			hero_npc_id[key2] = val["id"]

for key, val in hero_abilities.iteritems():
	for ability in val["abilities"]:
		for key2, val2 in abilities.iteritems():
			if key2 == ability:
				info = {}
				info["hero_id"] = hero_npc_id[key]
				info["ability_name"] = key2
				info["ability_info"] = val2
				# info["ability_info"].pop("img", None)
				info["ability_info"]["img"] = "dota2assets/img/spellicons/"+key2+".png"
				hero_ability[key2] = info

	# for key2, val2, in abilities.iteritems():
	# 	if key in val2["abilities"]:
	# 		info = {}
	# 		info["hero_id"] = hero_npc_id[key2]
	# 		info["ability_name"] = key
	# 		info["ability_info"] = val
	# 		hero_ability[key] = info


with open('hero_abilities2.json', 'wb') as filepath:
        json.dump(hero_ability, filepath, indent=4, sort_keys=False)

# for key, val in abilities.iteritems():
# 	for key2, val2 in val.iteritems():
# 		if key2 not in key_list:
# 			key_list.append(key2)

# print key_list
