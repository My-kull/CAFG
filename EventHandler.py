import CAFG_items
import random

from CAFG_items import janitor

#system global variables
current_score = 0
global_threat = 0
local_threat = {}
shop_items = []
#player global variables
time_units = 10
player_money = 1000
player_luck = 0
players_items = []
previous_travel_distance = 0
current_country = "" #change this to the starting country

#handlers that perform the basic functions

#handles the holistic airport visits
def turnhandler():
    timeunitrefresher()
    itemchecker()
    shoprandomiser(3)
    globalthreathandler()
    localthreathandler(0,0) #increases local threat using time units
    timehandler(0,0)
    eventhandler(local_threat, player_luck)
    actionhandler()
    movementhandler()

def globalthreathandler():
    #handles global_threat
    global current_country
    #!!!!!PLACEHOLDER!!!!!
    #!!!!!UPDATE THIS WITH THE country.name FROM THE DATABASE USING THE PATH airport.iso_country = country.iso_country!!!!!
    current_country = "France"
    global global_threat
    global_threat += previous_travel_distance * 1 #formula for increasing global threat
    return

def localthreathandler(timespent,threat):
    global local_threat
    if not local_threat.get(current_country): #Checks if country has an assigned local_threat in [dict] yet. If not, adds one.
        if len(local_threat.keys())==0:
            local_threat.update({current_country: 0})
        local_threat.update({current_country: 0})

    local_threat.update({current_country: local_threat.get(current_country)+(threat*timespent)}) #Increase local_threat for current country.

def timehandler(timespent,threat):
    global time_units
    time_units -= timespent
    localthreathandler(timespent,threat)


#handles the arrival events
def eventhandler(threat, luck):
    #vv THESE MULTIPLIERS ARE PLACEHOLDERS vv
    event_luck = (local_threat.get(current_country) * 1) * (global_threat * 1) - (luck * 1)
    eventhandlersub(event_luck)

def eventhandlersub(event_luck):
    event_happening = random.randint(1,4)
    match event_happening:
        case 1:
            print("You gained your yearly tax returns... again?... YIPPII")
            global player_money
            player_money += 200
            return
        case 2:
            print("You found a bazaar in the basement of the airport! Time for a shopping spree!")
            shoprandomiser(5) #Shop has 5 random items instead of 3.
            return
        case 3:
            print("You spontaneously grew a moustache. You feel strangely at peace with the universe.")
            global time_units
            time_units += 2
        case 4:
            print("It's the anniversary of the airport! People are celebrating without a care in the world.")
            global local_threat
            local_threat.update({current_country: local_threat.get(current_country)-5}) #drops local_threat by 5 units
        case _:
            print("It's a very boring airport! One star out of five!")
            return

#handles the actions that the player can perform
def actionhandler():
    jobrandomiser()
    doingactions = True
    while doingactions:
        doingactions = actionhandlersub(input("Input command (? for a list of commands): "))

def actionhandlersub(command):
    print()
    match command:
        case "?":
            print("List of commands")
            listcommands()
            return True
        case "use":
            actionuse()
            return True
        case "buy":
            actionbuy()
            return True
        case "check":
            actioncheck()
            return True
        case "work":
            actionwork()
            return True
        case "chill":
            print("You chilled for a while")
            return True
        case "leave":
            print("Moving to the next country")
            return False

        #made these two as a debugging tool, can possibly be left in the game?
        case "localT":
            print(local_threat)
            return True
        case "globalT":
            print(global_threat)
            return True
        case "time":
            print(time_units)
            return True
        case _:
            print("Unknown command (? for a list of commands)")
            return True

#list of actions that the player can perform
def listcommands():
    print()
    print(f"{'use' :<10} ---  use your items")
    print(f"{'buy' :<10} ---  buy more items")
    print(f"{'check' :<10} ---  check you items")
    print(f"{'work' :<10} ---  work for money")
    print(f"{'chill' :<10} ---  just take it easy")
    print(f"{'leave' :<10} ---  go to the next airport")
    print(f"{'?' :<10} ---  check your commands")
    print()

#uses your items
def actionuse():
    if len(players_items) == 0:
        print("You have no items. Go buy some")
    else:
        print("Your items:")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        for item in players_items:
            print(f"{players_items.index(item)+1} {item.name}\n")
        print()

        continue_using = True
        while continue_using:
            item_to_use = (input("What item do you want to use (Type number or N to go back): "))
            if item_to_use == "N":
                continue_using = False
            else:
                actionusesub(item_to_use)

def actionusesub(used_item):
    # here the match case structure for item use
    # if used_item.use_time == 0: return
    # else
    match used_item:
        case "nuke":
            return
        case _:
            print("Unknown item")
            return

#buys more items
def actionbuy():
    global player_money, shop_items
    print(f"Your balance: {player_money}")
    print()
    list_of_item_names = []

    continue_using = True
    while continue_using:
        if len(shop_items) == 0:
            print("You bought all the items. You lament that your shopping time has ended.")
            continue_using = False
            continue
        for item in shop_items:
            print(f"{shop_items.index(item) + 1} {item.name}: {item.price}€")
            list_of_item_names.append(item.name)
        print()
        shop_item_number = input("What item do you want to buy (N to go back): ")
        if shop_item_number == "N":
            continue_using = False
        elif not shop_item_number.isdigit():
            print("Wrong input")
        elif 0 > int(shop_item_number) <= len(list_of_item_names):
            print("Wrong input")
        else:
            if shop_items[int(shop_item_number) - 1].price > player_money:
                print("The item is too expensive")
            else:
                bought_item = shop_items[int(shop_item_number) - 1]
                players_items.append(bought_item)
                player_money -= shop_items[int(shop_item_number) - 1].price
                timehandler(1,shop_items[int(shop_item_number) - 1].price) #uses 1 unit of time and increases local threat by 10 with said amount of time.
                shop_items.pop(int(shop_item_number) - 1)
                print(f"You bought {bought_item.name}")
                print(f"Your balance: {player_money}")
                print()

#onks tälle checkpricelle enää mitää käyttöö? Siis kauppaha jo printtaa niien hinnat oikein
def checkprice(item):
    #!!!!!!!!!!!!PLACEHOLDER!!!!!!!!!!!!
    return 100

#checks your items
def actioncheck():
    if len(players_items) == 0:
        print("You have no items. Go buy some")
    else:
        continue_using = True
        while continue_using:
            print("Your items:")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            for item in players_items:
                print(f"{item.name}\n"
                      f"{item.desc}\n"
                      f"___________________________________________________________________________")
            print()
            item_to_check = input("What item do you want to check (N to go back): ")
            if item_to_check == "N":
                continue_using = False
            else:
                pass
                #get item_to_check description

#allows you to do work
def actionwork():
    #PLACEHOLDER, REPLACE ONCE THERE'S MORE JOBS!
    print("'clean' to clean airport")
    print()
    job_to_do = input("What work do you want to do (N to go back): ")
    if job_to_do == "N":
        return
    else:
        print()
        actionworksub(job_to_do)

def actionworksub(used_job):
    match used_job:
        case "clean":
            global player_money
            worktime=int(input(print("How long do you want to work for?")))
            print("Cleaning the airport...")
            if janitor in players_items: #Gives extra money if player has janitors clothes
                player_money += 50*worktime
                print(f"You cleaned the airport for {50*worktime}€!")
                print(f"Your current balance is {player_money}€.")
            else:
                player_money += 20*worktime
                print(f"You cleaned the airport for {20*worktime}€...")
                print(f"Your current balance is {player_money}€.")
            timehandler(worktime,-5) #Uses worktime amount of time_units and decreases the local threat by -5 per spent unit.
            return
        case _:
            print("Unknown job")
            return

#checks for passive and active item effects at the start of the turn
def itemchecker():
    # !!!!!!!!!!!!PLACEHOLDER!!!!!!!!!!!!
    print("checking player items")
    return

#randomises shop at start of the turn
def shoprandomiser(amount_of_items):
    # !!!!!!!!!!!!PLACEHOLDER!!!!!!!!!!!!
    # UTILIZE LUCK IN THIS!!
    shop_items.clear()
    list_of_items = CAFG_items.shop_items
    for i in range(amount_of_items):
        shop_items.append(list_of_items[random.randint(0, len(list_of_items)-1)])
    return

#randomises jobs at the start of the turn
def jobrandomiser():
    return

#refreshesh usable time units at the start of the turn
def timeunitrefresher():
    global time_units
    time_units = 10

#handles the movement from country to country
def movementhandler():
    return

turnhandler()