
import dota2api
import csv
import json
from collections import OrderedDict

items_list = []

with open('heroes/heroes.json') as filepath:
 	heroes = json.load(filepath, object_pairs_hook=OrderedDict)


with open('heroes/npc_heroes.json') as filepath:
    npc_heroes = json.load(filepath, object_pairs_hook=OrderedDict)
#print heroes["1"]
 #item_dict = {}
 #for item in items_list:
 #	item_dict[item["id"]] = item["localized_name"]


test = [
    {"key": "Abaddon", "value": "dota2assets/img/heroes/abaddon.png"},
    {"key": "Underlord", "value": "dota2assets/img/heroes/abyssal_underlord.png"},
    {"key": "Alchemist", "value": "dota2assets/img/heroes/alchemist.png"},
    {"key": "Ancient Apparition", "value": "dota2assets/img/heroes/ancient_apparition.png"},
    {"key": "Anti-Mage", "value": "dota2assets/img/heroes/antimage.png"},
    {"key": "Arc Warden", "value": "dota2assets/img/heroes/arc_warden.png"},
    {"key": "Axe", "value": "dota2assets/img/heroes/axe.png"},
    {"key": "Bane", "value": "dota2assets/img/heroes/bane.png"},
    {"key": "Batrider", "value": "dota2assets/img/heroes/batrider.png"},
    {"key": "Beastmaster", "value": "dota2assets/img/heroes/beastmaster.png"},
    {"key": "Bloodseeker", "value": "dota2assets/img/heroes/bloodseeker.png"},
    {"key": "Bounty Hunter", "value": "dota2assets/img/heroes/bounty_hunter.png"},
    {"key": "Brewmaster", "value": "dota2assets/img/heroes/brewmaster.png"},
    {"key": "Bristleback", "value": "dota2assets/img/heroes/bristleback.png"},
    {"key": "Broodmother", "value": "dota2assets/img/heroes/broodmother.png"},
    {"key": "Centaur Warrunner", "value": "dota2assets/img/heroes/centaur.png"},
    {"key": "Chaos Knight", "value": "dota2assets/img/heroes/chaos_knight.png"},
    {"key": "Chen", "value": "dota2assets/img/heroes/chen.png"},
    {"key": "Clinkz", "value": "dota2assets/img/heroes/clinkz.png"},
    {"key": "Crystal Maiden", "value": "dota2assets/img/heroes/crystal_maiden.png"},
    {"key": "Dark Seer", "value": "dota2assets/img/heroes/dark_seer.png"},
    {"key": "Dazzle", "value": "dota2assets/img/heroes/dazzle.png"},
    {"key": "Death Prophet", "value": "dota2assets/img/heroes/death_prophet.png"},
    {"key": "Disruptor", "value": "dota2assets/img/heroes/disruptor.png"},
    {"key": "Doom", "value": "dota2assets/img/heroes/doom_bringer.png"},
    {"key": "Dragon Knight", "value": "dota2assets/img/heroes/dragon_knight.png"},
    {"key": "Drow Ranger", "value": "dota2assets/img/heroes/drow_ranger.png"},
    {"key": "Earthshaker", "value": "dota2assets/img/heroes/earthshaker.png"},
    {"key": "Earth Spirit", "value": "dota2assets/img/heroes/earth_spirit.png"},
    {"key": "Elder Titan", "value": "dota2assets/img/heroes/elder_titan.png"},
    {"key": "Ember Spirit", "value": "dota2assets/img/heroes/ember_spirit.png"},
    {"key": "Enchantress", "value": "dota2assets/img/heroes/enchantress.png"},
    {"key": "Enigma", "value": "dota2assets/img/heroes/enigma.png"},
    {"key": "Faceless Void", "value": "dota2assets/img/heroes/faceless_void.png"},
    {"key": "Nature's Prophet", "value": "dota2assets/img/heroes/furion.png"},
    {"key": "Gyrocopter", "value": "dota2assets/img/heroes/gyrocopter.png"},
    {"key": "Huskar", "value": "dota2assets/img/heroes/huskar.png"},
    {"key": "Invoker", "value": "dota2assets/img/heroes/invoker.png"},
    {"key": "Jakiro", "value": "dota2assets/img/heroes/jakiro.png"},
    {"key": "Juggernaut", "value": "dota2assets/img/heroes/juggernaut.png"},
    {"key": "Keeper of the Light", "value": "dota2assets/img/heroes/keeper_of_the_light.png"},
    {"key": "Kunkka", "value": "dota2assets/img/heroes/kunkka.png"},
    {"key": "Legion Commander", "value": "dota2assets/img/heroes/legion_commander.png"},
    {"key": "Leshrac", "value": "dota2assets/img/heroes/leshrac.png"},
    {"key": "Lich", "value": "dota2assets/img/heroes/lich.png"},
    {"key": "Lifestealer", "value": "dota2assets/img/heroes/life_stealer.png"},
    {"key": "Lina", "value": "dota2assets/img/heroes/lina.png"},
    {"key": "Lion", "value": "dota2assets/img/heroes/lion.png"},
    {"key": "Lone Druid", "value": "dota2assets/img/heroes/lone_druid.png"},
    {"key": "Luna", "value": "dota2assets/img/heroes/luna.png"},
    {"key": "Lycan", "value": "dota2assets/img/heroes/lycan.png"},
    {"key": "Magnus", "value": "dota2assets/img/heroes/magnataur.png"},
    {"key": "Medusa", "value": "dota2assets/img/heroes/medusa.png"},
    {"key": "Meepo", "value": "dota2assets/img/heroes/meepo.png"},
    {"key": "Mirana", "value": "dota2assets/img/heroes/mirana.png"},
    {"key": "Monkey King", "value": "dota2assets/img/heroes/monkey_king.png"},
    {"key": "Morphling", "value": "dota2assets/img/heroes/morphling.png"},
    {"key": "Naga Siren", "value": "dota2assets/img/heroes/naga_siren.png"},
    {"key": "Necrophos", "value": "dota2assets/img/heroes/necrolyte.png"},
    {"key": "Shadow Fiend", "value": "dota2assets/img/heroes/nevermore.png"},
    {"key": "Night Stalker", "value": "dota2assets/img/heroes/night_stalker.png"},
    {"key": "Nyx Assassin", "value": "dota2assets/img/heroes/nyx_assassin.png"},
    {"key": "Outworld Devourer", "value": "dota2assets/img/heroes/obsidian_destroyer.png"},
    {"key": "Ogre Magi", "value": "dota2assets/img/heroes/ogre_magi.png"},
    {"key": "Omniknight", "value": "dota2assets/img/heroes/omniknight.png"},
    {"key": "Oracle", "value": "dota2assets/img/heroes/oracle.png"},
    {"key": "Phantom Assassin", "value": "dota2assets/img/heroes/phantom_assassin.png"},
    {"key": "Phantom Lancer", "value": "dota2assets/img/heroes/phantom_lancer.png"},
    {"key": "Phoenix", "value": "dota2assets/img/heroes/phoenix.png"},
    {"key": "Puck", "value": "dota2assets/img/heroes/puck.png"},
    {"key": "Pudge", "value": "dota2assets/img/heroes/pudge.png"},
    {"key": "Pugna", "value": "dota2assets/img/heroes/pugna.png"},
    {"key": "Queen of Pain", "value": "dota2assets/img/heroes/queenofpain.png"},
    {"key": "Clockwerk", "value": "dota2assets/img/heroes/rattletrap.png"},
    {"key": "Razor", "value": "dota2assets/img/heroes/razor.png"},
    {"key": "Riki", "value": "dota2assets/img/heroes/riki.png"},
    {"key": "Rubick", "value": "dota2assets/img/heroes/rubick.png"},
    {"key": "Sand King", "value": "dota2assets/img/heroes/sand_king.png"},
    {"key": "Shadow Demon", "value": "dota2assets/img/heroes/shadow_demon.png"},
    {"key": "Shadow Shaman", "value": "dota2assets/img/heroes/shadow_shaman.png"},
    {"key": "Timbersaw", "value": "dota2assets/img/heroes/shredder.png"},
    {"key": "Silencer", "value": "dota2assets/img/heroes/silencer.png"},
    {"key": "Wraith King", "value": "dota2assets/img/heroes/skeleton_king.png"},
    {"key": "Skywrath Mage", "value": "dota2assets/img/heroes/skywrath_mage.png"},
    {"key": "Slardar", "value": "dota2assets/img/heroes/slardar.png"},
    {"key": "Slark", "value": "dota2assets/img/heroes/slark.png"},
    {"key": "Sniper", "value": "dota2assets/img/heroes/sniper.png"},
    {"key": "Spectre", "value": "dota2assets/img/heroes/spectre.png"},
    {"key": "Spirit Breaker", "value": "dota2assets/img/heroes/spirit_breaker.png"},
    {"key": "Storm Spirit", "value": "dota2assets/img/heroes/storm_spirit.png"},
    {"key": "Sven", "value": "dota2assets/img/heroes/sven.png"},
    {"key": "Techies", "value": "dota2assets/img/heroes/techies.png"},
    {"key": "Templar Assassin", "value": "dota2assets/img/heroes/templar_assassin.png"},
    {"key": "Terrorblade", "value": "dota2assets/img/heroes/terrorblade.png"},
    {"key": "Tidehunter", "value": "dota2assets/img/heroes/tidehunter.png"},
    {"key": "Tinker", "value": "dota2assets/img/heroes/tinker.png"},
    {"key": "Tiny", "value": "dota2assets/img/heroes/tiny.png"},
    {"key": "Treant Protector", "value": "dota2assets/img/heroes/treant.png"},
    {"key": "Troll Warlord", "value": "dota2assets/img/heroes/troll_warlord.png"},
    {"key": "Tusk", "value": "dota2assets/img/heroes/tusk.png"},
    {"key": "Undying", "value": "dota2assets/img/heroes/undying.png"},
    {"key": "Ursa", "value": "dota2assets/img/heroes/ursa.png"},
    {"key": "Vengeful Spirit", "value": "dota2assets/img/heroes/vengefulspirit.png"},
    {"key": "Venomancer", "value": "dota2assets/img/heroes/venomancer.png"},
    {"key": "Viper", "value": "dota2assets/img/heroes/viper.png"},
    {"key": "Visage", "value": "dota2assets/img/heroes/visage.png"},
    {"key": "Warlock", "value": "dota2assets/img/heroes/warlock.png"},
    {"key": "Weaver", "value": "dota2assets/img/heroes/weaver.png"},
    {"key": "Windranger", "value": "dota2assets/img/heroes/windrunner.png"},
    {"key": "Winter Wyvern", "value": "dota2assets/img/heroes/winter_wyvern.png"},
    {"key": "Io", "value": "dota2assets/img/heroes/wisp.png"},
    {"key": "Witch Doctor", "value": "dota2assets/img/heroes/witch_doctor.png"},
    {"key": "Zeus", "value": "dota2assets/img/heroes/zuus.png"}
]

test2 = [
    {"key": "Abaddon", "value": "dota2assets/webm/heroes/abaddon.webm"},
    {"key": "Underlord", "value": "dota2assets/webm/heroes/abyssal_underlord.webm"},
    {"key": "Alchemist", "value": "dota2assets/webm/heroes/alchemist.webm"},
    {"key": "Ancient Apparition", "value": "dota2assets/webm/heroes/ancient_apparition.webm"},
    {"key": "Anti-Mage", "value": "dota2assets/webm/heroes/antimage.webm"},
    {"key": "Arc Warden", "value": "dota2assets/webm/heroes/arc_warden.webm"},
    {"key": "Axe", "value": "dota2assets/webm/heroes/axe.webm"},
    {"key": "Bane", "value": "dota2assets/webm/heroes/bane.webm"},
    {"key": "Batrider", "value": "dota2assets/webm/heroes/batrider.webm"},
    {"key": "Beastmaster", "value": "dota2assets/webm/heroes/beastmaster.webm"},
    {"key": "Bloodseeker", "value": "dota2assets/webm/heroes/bloodseeker.webm"},
    {"key": "Bounty Hunter", "value": "dota2assets/webm/heroes/bounty_hunter.webm"},
    {"key": "Brewmaster", "value": "dota2assets/webm/heroes/brewmaster.webm"},
    {"key": "Bristleback", "value": "dota2assets/webm/heroes/bristleback.webm"},
    {"key": "Broodmother", "value": "dota2assets/webm/heroes/broodmother.webm"},
    {"key": "Centaur Warrunner", "value": "dota2assets/webm/heroes/centaur.webm"},
    {"key": "Chaos Knight", "value": "dota2assets/webm/heroes/chaos_knight.webm"},
    {"key": "Chen", "value": "dota2assets/webm/heroes/chen.webm"},
    {"key": "Clinkz", "value": "dota2assets/webm/heroes/clinkz.webm"},
    {"key": "Crystal Maiden", "value": "dota2assets/webm/heroes/crystal_maiden.webm"},
    {"key": "Dark Seer", "value": "dota2assets/webm/heroes/dark_seer.webm"},
    {"key": "Dazzle", "value": "dota2assets/webm/heroes/dazzle.webm"},
    {"key": "Death Prophet", "value": "dota2assets/webm/heroes/death_prophet.webm"},
    {"key": "Disruptor", "value": "dota2assets/webm/heroes/disruptor.webm"},
    {"key": "Doom", "value": "dota2assets/webm/heroes/doom_bringer.webm"},
    {"key": "Dragon Knight", "value": "dota2assets/webm/heroes/dragon_knight.webm"},
    {"key": "Drow Ranger", "value": "dota2assets/webm/heroes/drow_ranger.webm"},
    {"key": "Earthshaker", "value": "dota2assets/webm/heroes/earthshaker.webm"},
    {"key": "Earth Spirit", "value": "dota2assets/webm/heroes/earth_spirit.webm"},
    {"key": "Elder Titan", "value": "dota2assets/webm/heroes/elder_titan.webm"},
    {"key": "Ember Spirit", "value": "dota2assets/webm/heroes/ember_spirit.webm"},
    {"key": "Enchantress", "value": "dota2assets/webm/heroes/enchantress.webm"},
    {"key": "Enigma", "value": "dota2assets/webm/heroes/enigma.webm"},
    {"key": "Faceless Void", "value": "dota2assets/webm/heroes/faceless_void.webm"},
    {"key": "Nature's Prophet", "value": "dota2assets/webm/heroes/furion.webm"},
    {"key": "Gyrocopter", "value": "dota2assets/webm/heroes/gyrocopter.webm"},
    {"key": "Huskar", "value": "dota2assets/webm/heroes/huskar.webm"},
    {"key": "Invoker", "value": "dota2assets/webm/heroes/invoker.webm"},
    {"key": "Jakiro", "value": "dota2assets/webm/heroes/jakiro.webm"},
    {"key": "Juggernaut", "value": "dota2assets/webm/heroes/juggernaut.webm"},
    {"key": "Keeper of the Light", "value": "dota2assets/webm/heroes/keeper_of_the_light.webm"},
    {"key": "Kunkka", "value": "dota2assets/webm/heroes/kunkka.webm"},
    {"key": "Legion Commander", "value": "dota2assets/webm/heroes/legion_commander.webm"},
    {"key": "Leshrac", "value": "dota2assets/webm/heroes/leshrac.webm"},
    {"key": "Lich", "value": "dota2assets/webm/heroes/lich.webm"},
    {"key": "Lifestealer", "value": "dota2assets/webm/heroes/life_stealer.webm"},
    {"key": "Lina", "value": "dota2assets/webm/heroes/lina.webm"},
    {"key": "Lion", "value": "dota2assets/webm/heroes/lion.webm"},
    {"key": "Lone Druid", "value": "dota2assets/webm/heroes/lone_druid.webm"},
    {"key": "Luna", "value": "dota2assets/webm/heroes/luna.webm"},
    {"key": "Lycan", "value": "dota2assets/webm/heroes/lycan.webm"},
    {"key": "Magnus", "value": "dota2assets/webm/heroes/magnataur.webm"},
    {"key": "Medusa", "value": "dota2assets/webm/heroes/medusa.webm"},
    {"key": "Meepo", "value": "dota2assets/webm/heroes/meepo.webm"},
    {"key": "Mirana", "value": "dota2assets/webm/heroes/mirana.webm"},
    {"key": "Monkey King", "value": "dota2assets/webm/heroes/monkey_king.webm"},
    {"key": "Morphling", "value": "dota2assets/webm/heroes/morphling.webm"},
    {"key": "Naga Siren", "value": "dota2assets/webm/heroes/naga_siren.webm"},
    {"key": "Necrophos", "value": "dota2assets/webm/heroes/necrolyte.webm"},
    {"key": "Shadow Fiend", "value": "dota2assets/webm/heroes/nevermore.webm"},
    {"key": "Night Stalker", "value": "dota2assets/webm/heroes/night_stalker.webm"},
    {"key": "Nyx Assassin", "value": "dota2assets/webm/heroes/nyx_assassin.webm"},
    {"key": "Outworld Devourer", "value": "dota2assets/webm/heroes/obsidian_destroyer.webm"},
    {"key": "Ogre Magi", "value": "dota2assets/webm/heroes/ogre_magi.webm"},
    {"key": "Omniknight", "value": "dota2assets/webm/heroes/omniknight.webm"},
    {"key": "Oracle", "value": "dota2assets/webm/heroes/oracle.webm"},
    {"key": "Phantom Assassin", "value": "dota2assets/webm/heroes/phantom_assassin.webm"},
    {"key": "Phantom Lancer", "value": "dota2assets/webm/heroes/phantom_lancer.webm"},
    {"key": "Phoenix", "value": "dota2assets/webm/heroes/phoenix.webm"},
    {"key": "Puck", "value": "dota2assets/webm/heroes/puck.webm"},
    {"key": "Pudge", "value": "dota2assets/webm/heroes/pudge.webm"},
    {"key": "Pugna", "value": "dota2assets/webm/heroes/pugna.webm"},
    {"key": "Queen of Pain", "value": "dota2assets/webm/heroes/queenofpain.webm"},
    {"key": "Clockwerk", "value": "dota2assets/webm/heroes/rattletrap.webm"},
    {"key": "Razor", "value": "dota2assets/webm/heroes/razor.webm"},
    {"key": "Riki", "value": "dota2assets/webm/heroes/riki.webm"},
    {"key": "Rubick", "value": "dota2assets/webm/heroes/rubick.webm"},
    {"key": "Sand King", "value": "dota2assets/webm/heroes/sand_king.webm"},
    {"key": "Shadow Demon", "value": "dota2assets/webm/heroes/shadow_demon.webm"},
    {"key": "Shadow Shaman", "value": "dota2assets/webm/heroes/shadow_shaman.webm"},
    {"key": "Timbersaw", "value": "dota2assets/webm/heroes/shredder.webm"},
    {"key": "Silencer", "value": "dota2assets/webm/heroes/silencer.webm"},
    {"key": "Wraith King", "value": "dota2assets/webm/heroes/skeleton_king.webm"},
    {"key": "Skywrath Mage", "value": "dota2assets/webm/heroes/skywrath_mage.webm"},
    {"key": "Slardar", "value": "dota2assets/webm/heroes/slardar.webm"},
    {"key": "Slark", "value": "dota2assets/webm/heroes/slark.webm"},
    {"key": "Sniper", "value": "dota2assets/webm/heroes/sniper.webm"},
    {"key": "Spectre", "value": "dota2assets/webm/heroes/spectre.webm"},
    {"key": "Spirit Breaker", "value": "dota2assets/webm/heroes/spirit_breaker.webm"},
    {"key": "Storm Spirit", "value": "dota2assets/webm/heroes/storm_spirit.webm"},
    {"key": "Sven", "value": "dota2assets/webm/heroes/sven.webm"},
    {"key": "Techies", "value": "dota2assets/webm/heroes/techies.webm"},
    {"key": "Templar Assassin", "value": "dota2assets/webm/heroes/templar_assassin.webm"},
    {"key": "Terrorblade", "value": "dota2assets/webm/heroes/terrorblade.webm"},
    {"key": "Tidehunter", "value": "dota2assets/webm/heroes/tidehunter.webm"},
    {"key": "Tinker", "value": "dota2assets/webm/heroes/tinker.webm"},
    {"key": "Tiny", "value": "dota2assets/webm/heroes/tiny.webm"},
    {"key": "Treant Protector", "value": "dota2assets/webm/heroes/treant.webm"},
    {"key": "Troll Warlord", "value": "dota2assets/webm/heroes/troll_warlord.webm"},
    {"key": "Tusk", "value": "dota2assets/webm/heroes/tusk.webm"},
    {"key": "Undying", "value": "dota2assets/webm/heroes/undying.webm"},
    {"key": "Ursa", "value": "dota2assets/webm/heroes/ursa.webm"},
    {"key": "Vengeful Spirit", "value": "dota2assets/webm/heroes/vengefulspirit.webm"},
    {"key": "Venomancer", "value": "dota2assets/webm/heroes/venomancer.webm"},
    {"key": "Viper", "value": "dota2assets/webm/heroes/viper.webm"},
    {"key": "Visage", "value": "dota2assets/webm/heroes/visage.webm"},
    {"key": "Warlock", "value": "dota2assets/webm/heroes/warlock.webm"},
    {"key": "Weaver", "value": "dota2assets/webm/heroes/weaver.webm"},
    {"key": "Windranger", "value": "dota2assets/webm/heroes/windrunner.webm"},
    {"key": "Winter Wyvern", "value": "dota2assets/webm/heroes/winter_wyvern.webm"},
    {"key": "Io", "value": "dota2assets/webm/heroes/wisp.webm"},
    {"key": "Witch Doctor", "value": "dota2assets/webm/heroes/witch_doctor.webm"},
    {"key": "Zeus", "value": "dota2assets/webm/heroes/zuus.webm"}
]

test3 = [
    {"key": "Abaddon", "value": "dota2assets/img/miniheroes/abaddon.png"},
    {"key": "Underlord", "value": "dota2assets/img/miniheroes/abyssal_underlord.png"},
    {"key": "Alchemist", "value": "dota2assets/img/miniheroes/alchemist.png"},
    {"key": "Ancient Apparition", "value": "dota2assets/img/miniheroes/ancient_apparition.png"},
    {"key": "Anti-Mage", "value": "dota2assets/img/miniheroes/antimage.png"},
    {"key": "Arc Warden", "value": "dota2assets/img/miniheroes/arc_warden.png"},
    {"key": "Axe", "value": "dota2assets/img/miniheroes/axe.png"},
    {"key": "Bane", "value": "dota2assets/img/miniheroes/bane.png"},
    {"key": "Batrider", "value": "dota2assets/img/miniheroes/batrider.png"},
    {"key": "Beastmaster", "value": "dota2assets/img/miniheroes/beastmaster.png"},
    {"key": "Bloodseeker", "value": "dota2assets/img/miniheroes/bloodseeker.png"},
    {"key": "Bounty Hunter", "value": "dota2assets/img/miniheroes/bounty_hunter.png"},
    {"key": "Brewmaster", "value": "dota2assets/img/miniheroes/brewmaster.png"},
    {"key": "Bristleback", "value": "dota2assets/img/miniheroes/bristleback.png"},
    {"key": "Broodmother", "value": "dota2assets/img/miniheroes/broodmother.png"},
    {"key": "Centaur Warrunner", "value": "dota2assets/img/miniheroes/centaur.png"},
    {"key": "Chaos Knight", "value": "dota2assets/img/miniheroes/chaos_knight.png"},
    {"key": "Chen", "value": "dota2assets/img/miniheroes/chen.png"},
    {"key": "Clinkz", "value": "dota2assets/img/miniheroes/clinkz.png"},
    {"key": "Crystal Maiden", "value": "dota2assets/img/miniheroes/crystal_maiden.png"},
    {"key": "Dark Seer", "value": "dota2assets/img/miniheroes/dark_seer.png"},
    {"key": "Dazzle", "value": "dota2assets/img/miniheroes/dazzle.png"},
    {"key": "Death Prophet", "value": "dota2assets/img/miniheroes/death_prophet.png"},
    {"key": "Disruptor", "value": "dota2assets/img/miniheroes/disruptor.png"},
    {"key": "Doom", "value": "dota2assets/img/miniheroes/doom_bringer.png"},
    {"key": "Dragon Knight", "value": "dota2assets/img/miniheroes/dragon_knight.png"},
    {"key": "Drow Ranger", "value": "dota2assets/img/miniheroes/drow_ranger.png"},
    {"key": "Earthshaker", "value": "dota2assets/img/miniheroes/earthshaker.png"},
    {"key": "Earth Spirit", "value": "dota2assets/img/miniheroes/earth_spirit.png"},
    {"key": "Elder Titan", "value": "dota2assets/img/miniheroes/elder_titan.png"},
    {"key": "Ember Spirit", "value": "dota2assets/img/miniheroes/ember_spirit.png"},
    {"key": "Enchantress", "value": "dota2assets/img/miniheroes/enchantress.png"},
    {"key": "Enigma", "value": "dota2assets/img/miniheroes/enigma.png"},
    {"key": "Faceless Void", "value": "dota2assets/img/miniheroes/faceless_void.png"},
    {"key": "Nature's Prophet", "value": "dota2assets/img/miniheroes/furion.png"},
    {"key": "Gyrocopter", "value": "dota2assets/img/miniheroes/gyrocopter.png"},
    {"key": "Huskar", "value": "dota2assets/img/miniheroes/huskar.png"},
    {"key": "Invoker", "value": "dota2assets/img/miniheroes/invoker.png"},
    {"key": "Jakiro", "value": "dota2assets/img/miniheroes/jakiro.png"},
    {"key": "Juggernaut", "value": "dota2assets/img/miniheroes/juggernaut.png"},
    {"key": "Keeper of the Light", "value": "dota2assets/img/miniheroes/keeper_of_the_light.png"},
    {"key": "Kunkka", "value": "dota2assets/img/miniheroes/kunkka.png"},
    {"key": "Legion Commander", "value": "dota2assets/img/miniheroes/legion_commander.png"},
    {"key": "Leshrac", "value": "dota2assets/img/miniheroes/leshrac.png"},
    {"key": "Lich", "value": "dota2assets/img/miniheroes/lich.png"},
    {"key": "Lifestealer", "value": "dota2assets/img/miniheroes/life_stealer.png"},
    {"key": "Lina", "value": "dota2assets/img/miniheroes/lina.png"},
    {"key": "Lion", "value": "dota2assets/img/miniheroes/lion.png"},
    {"key": "Lone Druid", "value": "dota2assets/img/miniheroes/lone_druid.png"},
    {"key": "Luna", "value": "dota2assets/img/miniheroes/luna.png"},
    {"key": "Lycan", "value": "dota2assets/img/miniheroes/lycan.png"},
    {"key": "Magnus", "value": "dota2assets/img/miniheroes/magnataur.png"},
    {"key": "Medusa", "value": "dota2assets/img/miniheroes/medusa.png"},
    {"key": "Meepo", "value": "dota2assets/img/miniheroes/meepo.png"},
    {"key": "Mirana", "value": "dota2assets/img/miniheroes/mirana.png"},
    {"key": "Monkey King", "value": "dota2assets/img/miniheroes/monkey_king.png"},
    {"key": "Morphling", "value": "dota2assets/img/miniheroes/morphling.png"},
    {"key": "Naga Siren", "value": "dota2assets/img/miniheroes/naga_siren.png"},
    {"key": "Necrophos", "value": "dota2assets/img/miniheroes/necrolyte.png"},
    {"key": "Shadow Fiend", "value": "dota2assets/img/miniheroes/nevermore.png"},
    {"key": "Night Stalker", "value": "dota2assets/img/miniheroes/night_stalker.png"},
    {"key": "Nyx Assassin", "value": "dota2assets/img/miniheroes/nyx_assassin.png"},
    {"key": "Outworld Devourer", "value": "dota2assets/img/miniheroes/obsidian_destroyer.png"},
    {"key": "Ogre Magi", "value": "dota2assets/img/miniheroes/ogre_magi.png"},
    {"key": "Omniknight", "value": "dota2assets/img/miniheroes/omniknight.png"},
    {"key": "Oracle", "value": "dota2assets/img/miniheroes/oracle.png"},
    {"key": "Phantom Assassin", "value": "dota2assets/img/miniheroes/phantom_assassin.png"},
    {"key": "Phantom Lancer", "value": "dota2assets/img/miniheroes/phantom_lancer.png"},
    {"key": "Phoenix", "value": "dota2assets/img/miniheroes/phoenix.png"},
    {"key": "Puck", "value": "dota2assets/img/miniheroes/puck.png"},
    {"key": "Pudge", "value": "dota2assets/img/miniheroes/pudge.png"},
    {"key": "Pugna", "value": "dota2assets/img/miniheroes/pugna.png"},
    {"key": "Queen of Pain", "value": "dota2assets/img/miniheroes/queenofpain.png"},
    {"key": "Clockwerk", "value": "dota2assets/img/miniheroes/rattletrap.png"},
    {"key": "Razor", "value": "dota2assets/img/miniheroes/razor.png"},
    {"key": "Riki", "value": "dota2assets/img/miniheroes/riki.png"},
    {"key": "Rubick", "value": "dota2assets/img/miniheroes/rubick.png"},
    {"key": "Sand King", "value": "dota2assets/img/miniheroes/sand_king.png"},
    {"key": "Shadow Demon", "value": "dota2assets/img/miniheroes/shadow_demon.png"},
    {"key": "Shadow Shaman", "value": "dota2assets/img/miniheroes/shadow_shaman.png"},
    {"key": "Timbersaw", "value": "dota2assets/img/miniheroes/shredder.png"},
    {"key": "Silencer", "value": "dota2assets/img/miniheroes/silencer.png"},
    {"key": "Wraith King", "value": "dota2assets/img/miniheroes/skeleton_king.png"},
    {"key": "Skywrath Mage", "value": "dota2assets/img/miniheroes/skywrath_mage.png"},
    {"key": "Slardar", "value": "dota2assets/img/miniheroes/slardar.png"},
    {"key": "Slark", "value": "dota2assets/img/miniheroes/slark.png"},
    {"key": "Sniper", "value": "dota2assets/img/miniheroes/sniper.png"},
    {"key": "Spectre", "value": "dota2assets/img/miniheroes/spectre.png"},
    {"key": "Spirit Breaker", "value": "dota2assets/img/miniheroes/spirit_breaker.png"},
    {"key": "Storm Spirit", "value": "dota2assets/img/miniheroes/storm_spirit.png"},
    {"key": "Sven", "value": "dota2assets/img/miniheroes/sven.png"},
    {"key": "Techies", "value": "dota2assets/img/miniheroes/techies.png"},
    {"key": "Templar Assassin", "value": "dota2assets/img/miniheroes/templar_assassin.png"},
    {"key": "Terrorblade", "value": "dota2assets/img/miniheroes/terrorblade.png"},
    {"key": "Tidehunter", "value": "dota2assets/img/miniheroes/tidehunter.png"},
    {"key": "Tinker", "value": "dota2assets/img/miniheroes/tinker.png"},
    {"key": "Tiny", "value": "dota2assets/img/miniheroes/tiny.png"},
    {"key": "Treant Protector", "value": "dota2assets/img/miniheroes/treant.png"},
    {"key": "Troll Warlord", "value": "dota2assets/img/miniheroes/troll_warlord.png"},
    {"key": "Tusk", "value": "dota2assets/img/miniheroes/tusk.png"},
    {"key": "Undying", "value": "dota2assets/img/miniheroes/undying.png"},
    {"key": "Ursa", "value": "dota2assets/img/miniheroes/ursa.png"},
    {"key": "Vengeful Spirit", "value": "dota2assets/img/miniheroes/vengefulspirit.png"},
    {"key": "Venomancer", "value": "dota2assets/img/miniheroes/venomancer.png"},
    {"key": "Viper", "value": "dota2assets/img/miniheroes/viper.png"},
    {"key": "Visage", "value": "dota2assets/img/miniheroes/visage.png"},
    {"key": "Warlock", "value": "dota2assets/img/miniheroes/warlock.png"},
    {"key": "Weaver", "value": "dota2assets/img/miniheroes/weaver.png"},
    {"key": "Windranger", "value": "dota2assets/img/miniheroes/windrunner.png"},
    {"key": "Winter Wyvern", "value": "dota2assets/img/miniheroes/winter_wyvern.png"},
    {"key": "Io", "value": "dota2assets/img/miniheroes/wisp.png"},
    {"key": "Witch Doctor", "value": "dota2assets/img/miniheroes/witch_doctor.png"},
    {"key": "Zeus", "value": "dota2assets/img/miniheroes/zuus.png"}
]


b = 0
c = []
for key, val in heroes.iteritems():
    found = False
    c.append(int(key))
    for item in test:
        if item["key"] == val["localized_name"]:
            b += 1
            val["img"] = item["value"]
            found = True
    if found == False:
        print val["localized_name"]

c.sort()

for key, val in heroes.iteritems():
    found = False
    for item in test2:
        if item["key"] == val["localized_name"]:
            b += 1
            val["webm"] = item["value"]
            found = True
    if found == False:
        print val["localized_name"]

for key, val in heroes.iteritems():
    found = False
    for item in test3:
        if item["key"] == val["localized_name"]:
            b += 1
            val["icon"] = item["value"]
            found = True
    if found == False:
        print val["localized_name"]

# get hero roles and role levels and complexity
for key, val in npc_heroes.iteritems():
    for key2, val2 in val.iteritems():
        rolesandrolelevels = {}
        try:
            roles = val2["Role"].split(",")
            rolelevels = val2["Rolelevels"].split(",")
            for role, rolelevel in zip(roles, rolelevels):
                rolesandrolelevels[role] = int(rolelevel)
            heroes[val2["HeroID"]]["roles"] = rolesandrolelevels
            heroes[val2["HeroID"]]["complexity"] = int(val2["Complexity"])
            print "SUCCESS"
        except Exception as e:
            print e

# for num in c:
#     heroes[str(num)]
hero_url_id = OrderedDict()

for key, val in heroes.iteritems():
    hero_url_id[val["url"]] = [key, val["localized_name"], val["webm"]]



# print c
print(heroes["68"]["img"], b, len(heroes))

with open('prod_jsons/drf_heroes.json', 'wb') as filepath:
        json.dump(heroes, filepath, indent=4, sort_keys=False)

with open('prod_jsons/drf_heroes_url_id.json', 'wb') as filepath:
        json.dump(hero_url_id, filepath, indent=4, sort_keys=True)

# print(type(heroes["1"]))
# print(type(heroes))
# for x, y in heroes.iteritems():
#     print(x)