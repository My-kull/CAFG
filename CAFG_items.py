class Item:
    pass
very_expensive = 1000
expensive = 500
costly = 100
cheap = 10
very_cheap = 2
free = 0


#About attribute.active: True means item is active, False means item is passive.
#About rarity

invis_cape = Item()
invis_cape.name = "Invisibility Cloack"
invis_cape.desc = "A cloack that makes you invisible.\nWhen used, splits the local threat level in two\n(-50% local threat.)."
invis_cape.rarity = "Harvinainen"
invis_cape.price = costly
invis_cape.use_time = 1
invis_cape.active = True
invis_cape.local_effect_p = 50

warhead = Item()
warhead.name = "Unstable Nuclear Warhead"
warhead.desc = "A Nuclear Warhead. Obviously no one wants to arrest a man with an armed bomb.\nDue to its unstable nature however, there is a 0.5% chance it will detonate.\n\x1B[3mOh and by the way, don't ask how you are allowed onto ANY planes with THIS...\x1B[0m\n(Local threat stays at 0, -5% global threat)"
warhead.rarity = "Erittäin Harvinainen"
warhead.price = free #it's free!
warhead.use_time = -1
warhead.active = False
warhead.local_effect = 0
warhead.global_effect_p = 0.05
warhead.detonation_chance = 0.005
#On a random turn= "The nuclear warhead is shaking!"
#throw d20= 2-20 = "Nothing happened...", 1 = "Game over"

lottery = Item()
lottery.name = "Falsified Lottery Coupon"
lottery.desc = "With your skills- I mean luck, you modify-\n*ahem* you SOMEHOW manage to get a lottery coupon with the winning numbers!\nLucky you!"
lottery.rarity = "Semi-harvinainen"
lottery.price = expensive
lottery.use_time = 1
lottery.type = True

luck_cookie = Item()
luck_cookie.name =  "Fortune Cookie"
luck_cookie.desc = "A traditional chinese cookie that tells your fortune!\n(+luck)"
luck_cookie.rarity = "Yleinen"
luck_cookie.price = cheap
luck_cookie.use_time = 1
luck_cookie.active = True

s_rabbit_paw = Item()
s_rabbit_paw.name = "Avaruusjäniksen käpälä"
s_rabbit_paw.desc = "Straight from the vast prairies of space."
s_rabbit_paw.rarity = "Harvinainen"
s_rabbit_paw.price = expensive
s_rabbit_paw.use_time = -1
s_rabbit_paw.active = True

janitor = Item()
janitor.name = "Janitors clothes"
janitor.desc = "Allows you to disguise yourself as a janitor and work for some money."
janitor.rarity = "Yleinen"
janitor.price = costly
janitor.use_time = -1
janitor.active = False

flightmaster = Item()
flightmaster.name = "Lennonjohtajan kuteet"
flightmaster.desc = "Allows you to disguise your self as a flight master\nand earn money while flying. Due to you not knowing how to fly however,\nthere is a slight chance you'll fall out of the sky(0.1%)."
flightmaster.rarity = "Harvinainen"
flightmaster.price = expensive
flightmaster.use_time = -1
flightmaster.active = False



tonnin_seteli = Item()
tonnin_seteli.name = "Kahvi + keksi"
tonnin_seteli.desc = "You think you may have gotten scammed...\nin fact you are pretty sure you did get scammed.\nYou did give a 1000€, right? There is no way it wasn't 1000€...\nIt was 1000€ you gave, didn't you? It was 1000€... \n\x1B[3m'Se oli tonnin seteli… enks mä antanu tonnin setelin?'\x1B[0m"
tonnin_seteli.rarity = "Erittäin harvinainen"
tonnin_seteli.price = 1000 #Tonnin seteli...
tonnin_seteli.use_time = -1
tonnin_seteli.active = False

print(warhead.desc)



