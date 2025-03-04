class Event:
    desc = ""
    rarity= ""
    location= ""
    def __init__(self,name):
        self.name = name

national_hero = Event("National Hero")
national_hero.desc = ""
national_hero.rarity = "Harvinainen"
national_hero.location = "everywhere"

space_express = Event("Space Express")
space_express.desc = "Gives a random item."
space_express.rarity = "Harvinainen"
space_express.location = "everywhere"