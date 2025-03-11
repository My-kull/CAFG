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
    buy = ""
    rarity = ""
    price = 0
    use_time = 0
    itemid = 0
    active = False
    def __init__(self, name):
        self.name = name


invis_cape = Item("Invisibility Cloak")
invis_cape.desc = ("A cloack that makes you invisible.\n"
                   "When used, splits the local threat level in two\n"
                   "\n"
                   "(-50% local threat.).")
invis_cape.buy = f"You imagine how easily you could've gotten away with stealing this instead."
invis_cape.rarity = "Harvinainen"
invis_cape.price = costly
invis_cape.use_time = 1
invis_cape.active = True
invis_cape.itemid = 1
#[local threat]/2 when used


lottery_fake = Item("Falsified Lottery Coupon")
lottery_fake.desc = ("With your skills- I mean luck, you modify-\n"
                "*ahem* you SOMEHOW manage to get a lottery coupon with the winning numbers!\n"
                "Lucky you!\n"
                "\n"
                "- Gives between 1 000€ and 3 000€, but increases local threat by 3 000 per use.")
lottery_fake.buy = f""
lottery_fake.rarity = "Semi-harvinainen"
lottery_fake.price = expensive
lottery_fake.use_time = 1
lottery_fake.type = True
lottery_fake.itemid = 2
#Gives 1000-3000€, threat up by 5 000 no matter the outcome.


lottery_coupon = Item("Legit Lottery Coupon")
lottery_coupon.desc = (f"An actually legit 100% real lottery coupon that's not gonna get you in trouble!\n"
                       f"May not give you a lot though...\n"
                       f"But theres a chance to get up to 10 000€! Statistically guaranteed after 10 000 coupons!!\n"
                       f"\n"
                       f"- 50% nothing,\n"
                       f"- ranging from 20% to 5% theres a chance to get from 1€ to 2000€,\n"
                       f"- 0.01% chance to get the jackpot of 10 000€)")
lottery_coupon.buy = "Surely this one's the one to make you rich! "
lottery_coupon.rarity = "Todella yleinen"
lottery_coupon.price = cheap
lottery_coupon.use_time = 1
lottery_coupon.active = True
lottery_coupon.itemid = 3
#50% chance to get nothing, 20% for 10-50€, 10% for 50-100€, 10% for 100-500€
# 5% for 500€-700€, 3% for 700€-1000, 1.99% for 1000-2000€, 0.01% 10 000€


luck_cookie = Item("Fortune Cookie")
luck_cookie.desc = ("A traditional chinese cookie that tells your fortune!\n"
                    "\n"
                    "+ luck")
luck_cookie.buy = ""
luck_cookie.rarity = "Yleinen"
luck_cookie.price = cheap
luck_cookie.use_time = 1
luck_cookie.active = True
luck_cookie.itemid = 4
#Increases luck, possibly add a small chance to decrease it instead?


energydrink = Item("ES :DDD")
energydrink.desc= (f"EbinSip the iconic energy drink.\n"
                   f"\n"
                   f"When consumed:\n"
                   f"- +4 time units")
energydrink.buy = "Ebin :DD"
energydrink.rarity = "Semi harvinainen"
energydrink.price = average
energydrink.use_time = 1
energydrink.active = True
energydrink.itemid = 5
#pärisemää :D


snow_globe = Item("Snow globe")
snow_globe.desc = ("A Snow globe suvenier.\n"
                   "Snow falls when you shake it, its fun to look at idk.\n"
                   "\n"
                   "+ 100 score")
snow_globe.buy = ""
snow_globe.rarity = "Harvinainen"
snow_globe.price = average
snow_globe.use_time = -1
snow_globe.active = False
snow_globe.itemid = 6
#score

arcade_ticket = Item("Arcade ticket")
arcade_ticket.desc = ("A ticket to the arcade where you can play games and have fun!\n"
                      "\n"
                      "+ 100 score")
arcade_ticket.buy = ""
arcade_ticket.rarity = "Semi harvinainen"
arcade_ticket.price = very_cheap
arcade_ticket.use_time = 1
arcade_ticket.active = True
arcade_ticket.itemid = 7
#scoreeeeeeeeeee

s_rabbit_paw = Item("Space-rabbit Foot")
s_rabbit_paw.desc = ("Straight from the vast prairies of space.\n"
                     "\n"
                     "+ luck")
s_rabbit_paw.buy = ""
s_rabbit_paw.rarity = "Harvinainen"
s_rabbit_paw.price = expensive
s_rabbit_paw.use_time = -1
s_rabbit_paw.active = False
s_rabbit_paw.itemid = 8
#Adds a certain % buff to luck.


janitor = Item("Janitors Clothes")
janitor.desc = ("Allows you to disguise yourself as a janitor and work for some money.\n"
                "\n"
                "- Increases income from [job]:'Clean the Airport' by 30€")
janitor.buy = ""
janitor.rarity = "Yleinen"
janitor.price = costly
janitor.use_time = -1
janitor.active = False
janitor.itemid = 9
#Under "Work", gives like 20€


flightmaster = Item("Flight-masters Clothes")
flightmaster.desc = ("Allows you to disguise your self as a flight master\n"
                     "and earn money while flying. Due to you not knowing how to fly however,\n"
                     "there is a slight chance you'll fall out of the sky.\n"
                     "\n"
                     "+ 200€ from the next flight\n"
                     "- 0.1% chance to die on the next flight.%")
flightmaster.buy = ""
flightmaster.rarity = "Harvinainen"
flightmaster.price = expensive
flightmaster.use_time = -1
flightmaster.active = False
flightmaster.itemid = 10
#Under "Work", gives like 100€


bulletvest = Item("Bulletproof Vest")
bulletvest.desc = ("Allows you to take more hits.\n"
                   "\n"
                   "(saves your life in some cases)")
bulletvest.buy = (f"The cashier gives you bombastic side eye and is probably thinking:\n"
                  f"'What'd you need that for?' You respond by giving the cashier back the bombastic side eye\n"
                  f"for selling such things in the first place.")
bulletvest.rarity = "Harvinainen"
bulletvest.price = expensive
bulletvest.use_time = 1
bulletvest.active = False
bulletvest.itemid = 11
#gives the player +50 health(once that is added)


tonnin_seteli = Item("A coffee and a cookie")
tonnin_seteli.desc = ("Wasn't this suppose to cost just 2€?\n"
                      "That was 1k € you gave, right? There is no way it wasn't 1k €...\n"
                      "But where's the change then? They couldn't possibly miss-calculate it, right?\n"
                      "They did give change back from it but it was so little...\n"
                      "Are you absolutely sure it was 1k € you gave? That was 1k €... \n"
                      "\n"
                      "\x1b[3m'Se oli tonnin seteli… Enks mä antanu tonnin setelin?'\x1b[0m")
tonnin_seteli.buy = (f"\x1b[3mYou find that 1000€ bill is the smallest you have so you decide to give it.\n"
                     f"The cashier gives very little change and then faces back to you.\n"
                     f"Although now he is just staring off into space with a blank expression on his face.\n"
                     f"You start to question if you actually gave 1000€ or not and try to ask several times-\n"
                     f"where the rest of the change is but you get no response. The cashier is like a statue.\n"
                     f"It's like his consciousness left this plane of existence. You wave your arm in front of him,\n"
                     f"but its no use. The money is gone now. No way to get it back.\n"
                     f"Are you certain it was actually 1000€ you gave? \x1b[0m")
tonnin_seteli.rarity = "Erittäin harvinainen"
tonnin_seteli.price = very_cheap  # Se oli tonnin seteli...
tonnin_seteli.use_time = -1
tonnin_seteli.active = False
tonnin_seteli.itemid = 12
#Does absolutely nothing, reference to 'Kummeli'

warhead = Item("Unstable Nuclear Warhead")
warhead.desc = ("A Nuclear Warhead. Obviously no one wants to arrest a man with an armed bomb.\n"
                "Due to its unstable nature however, there is a small chance it will detonate.\n"
                "\n"
                "\x1b[3mOh and by the way, don't ask how you are allowed onto ANY planes with THIS...\x1b[0m\n"
                "\n"
                "- Local threat stays at 0"
                "- -5% global threat"
                "- every turn, 5% chance to roll a D20. If it lands on 1 the warhead detonates ending the game.")
warhead.buy = "You can't believe you got this for free, it feels too good to be true."
warhead.rarity = "Erittäin Harvinainen"
warhead.price = free  # it's free!
warhead.use_time = -1
warhead.active = False
warhead.itemid = 13
#0.5% for game to end. Local threat stays at 0, global threat grows by -5%
#Alternatively: On start of a turn, theres ~1-5% to print= "The nuclear warhead is shaking!"
#Then game throws a d20= if 2-20 = print "Nothing happened...", if 1 = "Game over"



#these are the lists of items that the game uses
shop_items = [invis_cape, lottery_fake, lottery_coupon, luck_cookie, s_rabbit_paw, janitor, energydrink, tonnin_seteli, bulletvest]
qawason_items = [invis_cape, lottery_fake, lottery_coupon, luck_cookie, s_rabbit_paw, energydrink, bulletvest, flightmaster, warhead]
