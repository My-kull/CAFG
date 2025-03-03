import random

#system global variables
global_threat = 0
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
    shoprandomiser(5)
    threathandler()
    eventhandler(1, player_luck)
    actionhandler()
    movementhandler()

def threathandler():
    #handles
    global global_threat
    global_threat += previous_travel_distance * 1 #formula for increasing global threat
    return

#handles the arrival events
def eventhandler(local_threat, luck):
    event_luck = (local_threat * 1) * (global_threat * 1) - (luck * 1) #these multipliers are placeholders
    eventhandlersub(event_luck)

def eventhandlersub(event_luck):
    event_happening = random.randint(1,3)
    match event_happening:
        case 1:
            print("You gained your yearly tax returns... again?... YIPPII")
            global player_money
            player_money += 200
            return
        case 2:
            print("You found a bazaar in the basement of the airport! Time for a shopping spree!")
            shoprandomiser(7)
            return
        case 3:
            print("You spontaneously grew a moustache. You feel strangely at peace with the universe.")
            global time_units
            time_units =+ 2
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
        print("Your items")
        print()
        for item in players_items:
            print(item)
        print()

        continue_using = True
        while continue_using:
            item_to_use = (input("What item do you want to use (N to go back): "))
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
    global player_money
    print(f"Your balance: {player_money}")
    print()
    for item in shop_items:
        print(f"{item}: {checkprice(item)}€")
    print()

    continue_using = True
    while continue_using:
        item_to_buy = input("What item do you want to buy (N to go back): ")
        if item_to_buy == "N":
            continue_using = False
        else:
            if checkprice(item_to_buy) > player_money:
                print("The item is too expensive")
            else:
                players_items.append(item_to_buy)
                player_money -= checkprice(item_to_buy)
                print(f"You bought {item_to_buy}")
                print(f"Your balance: {player_money}")

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
            print("Your items")
            print()
            for item in players_items:
                print(item)
            print()
            item_to_check = input("What item do you want to check (N to go back): ")
            if item_to_check == "N":
                continue_using = False
            else:
                pass
                #get item_to_check description

#allows you to do work
def actionwork():
    print()
    #here list of jobs
    print()
    job_to_do = input("What work do you want to do (N to go back): ")
    if job_to_do == "N":
        return
    else:
        print()
        actionusesub(job_to_do)

def actionworksub(used_job):
    match used_job:
        case "clean":
            return
        case _:
            print("Unknown item")
            return

#checks for passive and active item effects at the start of the turn
def itemchecker():
    # !!!!!!!!!!!!PLACEHOLDER!!!!!!!!!!!!
    print("checking player items")
    return

#randomises shop at start of the turn
def shoprandomiser(amount_of_items):
    # !!!!!!!!!!!!PLACEHOLDER!!!!!!!!!!!!
    print("shop randomised")
    shop_items.clear()
    shop_items.extend(["cheese", "wine", "nuclear warhead", "bread"])
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