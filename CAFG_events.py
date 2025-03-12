class Event:
    desc = ""
    rarity= ""
    location= ""
    def __init__(self,name):
        self.name = name

#decreases gv.local_threat by set amount or %
fox_fires = Event("Northern Lights")
fox_fires.desc = "Northern lights can be seen in the sky."
fox_fires.rarity = "Semi Harvinainen"
fox_fires.location = "country dependent"


#Sets gv.local_threat to 0 if successful
national_hero = Event("National Hero")
national_hero.desc = "A terror attack is about to happen at the airport!"
national_hero.rarity = "Harvinainen"
national_hero.location = "everywhere"

#Gives a random item
space_express = Event("Space Express")
space_express.desc = "Your Qawason express package has arrived! You wonder when you ordered this..."
space_express.rarity = "Harvinainen"
space_express.location = "everywhere"

used_events=[national_hero, space_express, fox_fires]