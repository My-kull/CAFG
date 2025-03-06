class Event:
    desc = ""
    rarity= ""
    location= ""
    def __init__(self,name):
        self.name = name

#decreases local_threat by set amount or %
fox_fires = Event("Northern Lights")
fox_fires.desc = ""
fox_fires.rarity = "Semi Harvinainen"
fox_fires.location = "country dependent"


#Sets local_threat to 0 if successful
national_hero = Event("National Hero")
national_hero.desc = ""
national_hero.rarity = "Harvinainen"
national_hero.location = "everywhere"

#Gives a random item
space_express = Event("Space Express")
space_express.desc = ""
space_express.rarity = "Harvinainen"
space_express.location = "everywhere"