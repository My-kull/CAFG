import CAFG_items
import random


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
current_country = "France" #change this to the starting country
#part of the movementhandler placeholder
global_country_index = 0

#handlers that perform the basic functions

#handles the holistic airport visits
def turnhandler():
    while True:
        global current_score
        current_score += 100
        timeunitrefresher(10)
        itemchecker()
        shoprandomiser(3)
        globalthreathandler()
        localthreathandler(0,0) #increases local threat using time units
        timehandler(0,0)
        eventhandler(player_luck)
        actionhandler()
        movementhandler()

def globalthreathandler():
    #handles global_threat
    global current_country
    #!!!!!PLACEHOLDER!!!!!
    #!!!!!UPDATE THIS WITH THE country.name FROM THE DATABASE USING THE PATH airport.iso_country = country.iso_country!!!!!
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
def eventhandler(luck):
    #vv THESE MULTIPLIERS ARE PLACEHOLDERS vv
    event_luck = (local_threat.get(current_country) * 1) * (global_threat * 1) - (luck * 1)
    eventhandlersub(event_luck)

def eventhandlersub(event_luck):
    event_happening = random.randint(0,4)
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
            leaveornot = input("Do you want to leave the airport?(y/N): ")
            if leaveornot == "y":
                return False
            else:
                return True
        #made these two as a debugging tool, can possibly be left in the game?
        case "stats":
            checkstats()
            return True
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

#prints player and game stats
def checkstats():
    print("Game status")
    print(f"Score is {current_score}")
    print(f"Global threat is {global_threat}")
    print(f"Current country is {current_country}")
    print(f"Local treat is {local_threat.get(current_country)}")
    print()

    print("Your status")
    print(f"Your balance: {player_money}€")
    print(f"Your luck: {player_luck}")
    print(f"The timeunits you have: {time_units}")
    print()

#uses your items
def actionuse():
    if len(players_items) == 0:
        print("You have no items. Go buy some")
    else:
        print("Your items:")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        item_number = 0
        for item in players_items:
            print(f"{item_number + 1} {item.name}\n")
            item_number += 1
        print()

        continue_using = True
        while continue_using:
            item_to_use = input("What item do you want to use (Type number or N to go back): ")
            if item_to_use == "N":
                continue_using = False
            elif not item_to_use.isdigit():
                print()
                print("Wrong input!")
            else:
                actionusesub(item_to_use)

def actionusesub(used_item):
    # here the match case structure for item use
    use_item = players_items[int(used_item) - 1]
    print(f"You've decided to use {use_item.name}")
    global time_units, player_money, current_score, local_threat, player_luck
    if players_items[int(used_item) - 1].active:
        players_items.pop(int(used_item) - 1)
        print("Item used.")
        current_score += 50
        time_units -= 1
    else:
        print("Item is passive.")
    print()
    match use_item:
        case CAFG_items.lottery_fake:
            money = random.randint(1000, 3000)
            local_threat[current_country] += 3000 - (player_luck // 100)
            print(f"You manage to get {money}€, but now you are in trouble!")
            player_money += money
            return

        case CAFG_items.lottery_coupon:
            lottery = random.randint(0, 10000) + (player_luck // 100)
            if lottery <= 5000:
                money = 0
            elif 5000 < lottery < 7000:
                money = random.randint(1, 5)
            elif 7000 < lottery < 8000:
                money = random.randint(5, 10)
            elif 8000 < lottery < 9000:
                money = random.randint(10, 50)
            elif 9000 < lottery < 9500:
                money = random.randint(50, 100)
            elif 9500 < lottery < 9800:
                money = random.randint(100, 500)
            elif 9800 < lottery < 9999:
                money = random.randint(500, 2000)
            else:
                money = 10000
            print(f"Congratulations! You got {money}€ from the lottery!")
            player_money += money
            return

        case CAFG_items.invis_cape:
            local_threat[current_country] = local_threat[current_country] // 2
            print("The cape made you harder to track! (Decreased local threat by 50%)")
            return

        case CAFG_items.luck_cookie:
            chance = random.randint(1, 6)
            if chance == 1:
                player_luck += 10
                luck = 10
            else:
                player_luck -= 10
                luck = -10
            print(f"You read the fortune from the cookie and got {luck} luck!")
            return

        case CAFG_items.pot_brownie:
            addtime = 4
            time_units += addtime
            print(f"You eat the brownie...\n"
                  f"You feel like theres no longer a rush to anywhere anymore...\n"
                  f"(Gained {addtime} time units)")
            return

        case CAFG_items.tonnin_seteli:
            print(f"You ponder at the purchase. It cost you 1000€...\n"
                f"You've forgotten what the price was suppose to even be, why didn't the cashier give back any change?\n"
                f"Was it actually 1000€? Is this some special coffee? Or some caviar cookie?\n"
                f"Now you are questioning if you actually gave 1000€ for it or not...\n"
                f"You don't even feel like eating this...")
            return

        case CAFG_items.arcade_ticket:
            print(f"You visit a local arcade to play some games and have some fun! Yippee!")
            current_score += 100
            return

        case CAFG_items.snow_globe:
            print(f"You shake the snowglobe and watch the artificial snowflakes fall...\n"
                  f"...\n"
                  f"What fun!!!")
            current_score += 100
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
        item_number = 0
        for item in shop_items:
            print(f"{item_number + 1} {item.name}: {item.price}€")
            list_of_item_names.append(item.name)
            item_number+=1
        print()

        shop_item_number = input("What item do you want to buy (N to go back): ")
        if shop_item_number == "N":
            continue_using = False
        elif not shop_item_number.isdigit():
            print("Wrong input")
        elif 0 > int(shop_item_number) or len(list_of_item_names) <= int(shop_item_number):
            print("Wrong input")
        else:
            if shop_items[int(shop_item_number) - 1].price > player_money:
                print("The item is too expensive")
                print()
            else:
                bought_item = shop_items[int(shop_item_number) - 1]
                if bought_item == CAFG_items.tonnin_seteli:
                    player_money -= 996
                players_items.append(bought_item)
                player_money -= shop_items[int(shop_item_number) - 1].price
                timehandler(1,shop_items[int(shop_item_number) - 1].price) #uses 1 unit of time and increases local threat by 10 with said amount of time.
                shop_items.pop(int(shop_item_number) - 1)
                print()
                print(f"You bought {bought_item.name}")
                print(bought_item.buy)
                print()
                print(f"Your balance: {player_money}")
                print()

#checks your items
def actioncheck():
    if len(players_items) == 0:
        print("You have no items. Go buy some")
    else:

        print("Your items:")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        for item in players_items:
            print(f"{item.name}\n"
                  f"{item.desc}\n"
                  f"___________________________________________________________________________")
        print()

#allows you to do work
def actionwork():
    #PLACEHOLDER, REPLACE ONCE THERE'S MORE JOBS!
    print("'clean' to clean airport.")
    print("'rob' to rob a random person.")
    print()
    job_to_do = input("What work do you want to do (N to go back): ")
    if job_to_do == "N":
        return
    else:
        print()
        actionworksub(job_to_do)

def actionworksub(used_job):
    global player_money
    match used_job:
        case "clean":
            stopwork = False
            while not stopwork:
                worktime = input("How long do you want to work for?(N to go back): ")
                print()
                if worktime == "N":
                    print("You've decided you didn't want to clean the airport.")
                    stopwork = True
                elif not worktime.isdigit():
                    print("Invalid work time.")
                    print()
                else:
                    print("Cleaning the airport...")
                    if CAFG_items.janitor in players_items: #Gives extra money if player has janitors clothes
                        money = 50*int(worktime)
                        player_money += money
                        print(f"You cleaned the airport for {money}€!")
                        print(f"Your current balance is {player_money}€.")
                        stopwork=True
                    else:
                        money = 20*int(worktime)
                        player_money += money
                        print(f"You cleaned the airport for {money}€...")
                        print(f"Your current balance is {player_money}€.")
                        stopwork= True
                print()
                timehandler(int(worktime),-5) #Uses worktime amount of time_units and decreases the local threat by -5 per spent unit.
            return
        case "rob":
            robbed=random.randint(1+player_luck,200+player_luck)
            print(f"You robbed an random civilian for {robbed}€!")
            player_money += robbed
            # threat increases by 10 for every € stolen, player luck decreases this
            localthreathandler(1,robbed*(10-(int(player_luck/10))))
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
    for i in range(amount_of_items):
        shop_items.append(CAFG_items.shop_items[random.randint(0, len(CAFG_items.shop_items)-1)])
    return

#randomises jobs at the start of the turn
def jobrandomiser():
    #currently unused
    return

#refreshesh usable time units at the start of the turn
def timeunitrefresher(amount):
    global time_units
    time_units = amount

#handles the movement from country to country
def movementhandler():
    #placeholder, replace with real code
    choiceleaveorstay = ""
    while True:
        choiceleaveorstay = input("Do you want to stay in the country or leave the country?(leave/stay): ")
        if choiceleaveorstay == "leave" or choiceleaveorstay == "stay":
            break
    global current_score
    global previous_travel_distance
    global global_country_index
    global current_country
    list_of_countries = ["France", "Russia", "USA", "China",
                         "Japan", "Germany", "UK", "Australia",
                         "India", "Canada", "Spain", "Italy",
                         "Finland", "Turkey", "Brazil", "New Zealand"]
    if choiceleaveorstay == "leave":
        print("Moving to the next country")
        current_score += 300
        previous_travel_distance = 1000
        global_country_index += 1
        if global_country_index < len(list_of_countries):
            current_country = list_of_countries[global_country_index]
        else:
            global_country_index = 0
            current_country = list_of_countries[global_country_index]
    elif choiceleaveorstay == "leave":
        print("Moving to the next airport within the country")
        current_score += 100
        previous_travel_distance = 200
    else:
        print("Something went wrong")

#you are dead
def deathhandler():
    print()
    print("You are dead")
    print()
    print(f"Your final score is {current_score}")
    quit()

turnhandler()