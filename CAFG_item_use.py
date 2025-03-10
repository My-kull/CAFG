import random
import CAFG_items
import EventHandler


def use_item_match_super2k25_no_virus(item_name):
    if item_name.active:
        EventHandler.players_items.pop(item_name)
        print("Item used.")
        EventHandler.current_score += 50
        EventHandler.time_units -= 1
    else:
        print("Item is passive.")
    match item_name:
        case CAFG_items.lottery_fake:
            money = random.randint(1000, 3000)
            EventHandler.local_threat += 3000-(EventHandler.player_luck//100)
            print(f"You manage to get{money}€, but now you are in trouble!")
            EventHandler.player_money += money
            return

        case CAFG_items.lottery_coupon:
            lottery = random.randint(0, 10000)+(EventHandler.player_luck//100)
            if lottery <= 5000:
                money = 0
            elif 5000 < lottery < 7000:
                money = random.randint(10, 50)
            elif 7000 < lottery < 8000:
                money = random.randint(50, 100)
            elif 8000 < lottery < 9000:
                money = random.randint(100, 500)
            elif 9000 < lottery < 9500:
                money = random.randint(500, 700)
            elif 9500 < lottery < 9800:
                money = random.randint(700, 1000)
            elif 9800 < lottery < 9999:
                money = random.randint(1000, 2000)
            else:
                money = 10000
            print(f"Congratulations! You got {money}€ from the lottery!")
            EventHandler.player_money += money
            return

        case CAFG_items.invis_cape:
            EventHandler.local_threat = EventHandler.local_threat//2
            print("The cape made you harder to track! (Decreased local threat by 50%)")
            return

        case CAFG_items.luck_cookie:
            chance = random.randint(1, 6)
            if chance == 1:
                EventHandler.player_luck += 10
                luck = 10
            else:
                EventHandler.player_luck -= 10
                luck = -10
            print(f"You read the fortune from the cookie and got {luck} luck!")
            return

        case CAFG_items.pot_brownie:
            addtime = 4
            EventHandler.time_units += addtime
            print(f"You eat the brownie...\n"
                  f"You feel like theres no longer a rush to anywhere anymore.(+{addtime} time units)")
            return

        case CAFG_items.tonnin_seteli:
            print(f"You ponder at the purchase. It cost you 1000€...\n"
                  f"You've forgotten what the price was suppose to even be, why didn't the cashier give back any change?\n"
                  f"Was it actually 1000€? Is this some special coffee? Or some caviar cookie?\n"
                  f"Now you are questioning if you actually gave 1000€ for it or not...\n"
                  f"You don't even feel like eating this...")
            return

        case CAFG_items.arcade_ticket:
            print(f"You visit a local arcade to play some games and have some fun!")
            EventHandler.current_score += 100
            return

        case CAFG_items.snow_globe:
            print(f"You shake the snowglobe and watch the artificial snowflakes fall...\n"
                  f"What fun!")
            EventHandler.current_score += 100
            return