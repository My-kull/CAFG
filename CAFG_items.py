very_expensive = 1000
expensive = 500
costly = 100
average = 50
cheap = 10
very_cheap = 2
free = 0


# About attribute.rarity: Items rarity placeholder.
#   Rarities ranging from most common to most rare:
#       * Todella yleinen.
#       * Yleinen.
#       * Semi harvinainen.
#       * Harvinainen.
#       * Erittäin harvinainen.

# About attribute.price: price of the item, called values are at the very top of this file.

# About attribute.use_time: positive [int]s give items the corresponding amount of use times.
#   * Everytime an item is used, its value is updated as current value minus 1.
#   * Once 0 item cant be used anymore.
#   * -1 gives an infinite amount of use times.

# About attribute.active: True means item is active, False means item is passive.


class Item:
    desc = ""
    rarity = ""
    price = 0
    use_time = 0
    active = False
    def __init__(self, name):
        self.name = name


invis_cape = Item("Invisibility Cloak")
invis_cape.desc = ("A cloack that makes you invisible.\n"
                   "When used, splits the local threat level in two\n"
                   "\n"
                   "(-50% local threat.).")
invis_cape.rarity = "Harvinainen"
invis_cape.price = costly
invis_cape.use_time = 1
invis_cape.active = True
#[local threat]/2 when used

lottery = Item("Falsified Lottery Coupon")
lottery.desc = ("With your skills- I mean luck, you modify-\n"
                "*ahem* you SOMEHOW manage to get a lottery coupon with the winning numbers!\n"
                "Lucky you!\n"
                "\n"
                "(Gives like a 1000€)")  #PLACEHOLDER!!!!!!!!!!!!!!!!!!!!11
lottery.rarity = "Semi-harvinainen"
lottery.price = expensive
lottery.use_time = 1
lottery.type = True
#Gives like 1000€

luck_cookie = Item("Fortune Cookie")
luck_cookie.desc = ("A traditional chinese cookie that tells your fortune!\n"
                    "\n(+luck)")
luck_cookie.rarity = "Yleinen"
luck_cookie.price = cheap
luck_cookie.use_time = 1
luck_cookie.active = True
#Increases luck, possibly add a small chance to decrease it instead?

s_rabbit_paw = Item("Space-rabbit Foot")
s_rabbit_paw.desc = ("Straight from the vast prairies of space.\n"
                     "\n(+luck)")
s_rabbit_paw.rarity = "Harvinainen"
s_rabbit_paw.price = expensive
s_rabbit_paw.use_time = -1
s_rabbit_paw.active = True
#Adds a certain % buff to luck.

janitor = Item("Janitors Clothes")
janitor.desc = ("Allows you to disguise yourself as a janitor and work for some money.\n"
                "\n(Increases income from 'Clean Airport' [job])")
janitor.rarity = "Yleinen"
janitor.price = costly
janitor.use_time = -1
janitor.active = False
#Under "Work", gives like 20€

#below this, items are not used
flightmaster = Item("Flight-masters Clothes")
flightmaster.desc = ("Allows you to disguise your self as a flight master\n"
                     "and earn money while flying. Due to you not knowing how to fly however,\n"
                     "there is a slight chance you'll fall out of the sky.\n"
                     "\n"
                     "(0.1% chance to die on the next flight.)%")
flightmaster.rarity = "Harvinainen"
flightmaster.price = expensive
flightmaster.use_time = -1
flightmaster.active = False
#Under "Work", gives like 100€

bulletvest = Item("Bulletproof Vest")
bulletvest.desc = ""
bulletvest.rarity = "Harvinainen"
bulletvest.price = expensive
bulletvest.use_time = 5
bulletvest.active = True
#

tonnin_seteli = Item("Kahvi + keksi")
tonnin_seteli.desc = ("You think you may have gotten scammed...\n"
                      "in fact you are pretty sure you did get scammed.\n"
                      "You did give a 1000€, right? There is no way it wasn't 1000€...\n"
                      "It was 1000€ you gave, didn't you? It was 1000€... \n"
                      "\n"
                      "\x1b[3m'Se oli tonnin seteli… enks mä antanu tonnin setelin?'\x1b[0m")
tonnin_seteli.rarity = "Erittäin harvinainen"
tonnin_seteli.price = 1000  # Tonnin seteli...
tonnin_seteli.use_time = -1
tonnin_seteli.active = False
#Does absolutely nothing, reference to 'Kummeli'

warhead = Item("Unstable Nuclear Warhead")
warhead.desc = ("A Nuclear Warhead. Obviously no one wants to arrest a man with an armed bomb.\n"
                "Due to its unstable nature however, there is a 0.5% chance it will detonate.\n"
                "\n"
                "\x1b[3mOh and by the way, don't ask how you are allowed onto ANY planes with THIS...\x1b[0m\n"
                "\n"
                "(Local threat stays at 0, -5% global threat. 0.5% chance to end the game on each turn.)")
warhead.rarity = "Erittäin Harvinainen"
warhead.price = free  # it's free!
warhead.use_time = -1
warhead.active = False
#0.5% for game to end. Local threat stays at 0, global threat grows by -5%
#Alternatively: On start of a turn, theres ~1-5% to print= "The nuclear warhead is shaking!"
#Then game throws a d20= if 2-20 = print "Nothing happened...", if 1 = "Game over"

shop_items = [invis_cape, lottery, luck_cookie, s_rabbit_paw, janitor]

#for i in shop_items:
#   print(f"{i.name:<30} --- {i.price:>10}")

#for i in shop_items:
#    print(f"{i.name} \n {i.desc} \n -------------------------------------------------------------")