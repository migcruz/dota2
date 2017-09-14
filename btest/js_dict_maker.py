import json
from collections import OrderedDict

with open('heroes_url_id.json') as filepath:
 	heroes = json.load(filepath, object_pairs_hook=OrderedDict)


x = []
for key, val in heroes.iteritems():
	y = "<"+key+"<: [;"+val[0]+";,@"+val[2]+"`],"
	print y
	#x.append()