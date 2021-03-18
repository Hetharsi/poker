import poker
import random
import poker_rules
class Player:
    def __init__(s, name, player_ID):
        s.name = str(name)
        s.hand = []
        s.money = 1000
        s.moneyInRound = 0
        s.player_ID = int(player_ID)
        s.active = True
        s.inRound = True
        s.inGame = True
        s.raisePlayer = False
        s.previousDecision = "No decisision yet"
        s.previousRaise = 0
        s.previousSpentAll = 0
        s.keep = 0

    def keepPot(s, roundPot, minPayment):
        print(f"Min payment:  {minPayment}")
        s.active = False
        s.money -= minPayment
        s.moneyInRound += minPayment
        roundPot += minPayment
        s.previousDecision = "4"
        s.previousSpentAll = minPayment
        return (minPayment)
    def raise_pot(s, roundPot, minPayment):
        print("This is the money in the pool: " + str(roundPot))
        print("Your money: " + str(s.money))
        print("Minimum payment: "  +str(minPayment))
        pot = int(input("How much do you want to raise the pot"))
        s.previousRaise = pot
        s.money -= (pot + minPayment)
        s.moneyInRound += pot + minPayment
        s.raisePlayer = True
        s.previousDecision = "3"
        s.previousSpentAll += pot + minPayment
        return (pot+minPayment)
    def getName(s):
        print(s.name)

    def getBestHand(s):
        return poker_rules.findBestHand(s.hand)

    def passTurn(s,actualPot, minPayment):
        print("This is the money in the pool: " + str(actualPot))
        print("Your money: " + str(s.money))
        print("Minimum payment: "  +str(minPayment))
        print()
        s.money -= minPayment
        s.moneyInRound += minPayment
        s.active = False
        s.previousDecision = "1"

    def throwHand(s):
        print("Your money: " + str(s.money))
        s.active = False
        s.moneyInRound = 0
        s.inRound = False
        s.previousDecision = "2"



    def draw_card(s, deck):
        s.hand += [deck.pop(random.randint(0, len(deck)-1))]
        return (s.hand)

    def make_smallBlind(s):
        s.smallBlind = True

    def make_bigBlind(s):
        s.bigBlind = True

    def remake_smallBlind(s):
        s.smallBlind = False

    def remake_bigBlind(s):
        s.bigBlind = False


    def playerInformation(s, actualPot, minPayment):
        print("--------------------------")
        print("NAME:           " + s.name)
        print("ID:             " + str(s.player_ID))
        print("MONEY:          " + str(s.money))
        print("MONEY IN ROUND: " + str(s.moneyInRound))
        print("INGAME:         " + str(s.inGame))
        print("INROUND:        " + str(s.inRound))
        print("INROUND-ACTIVE: " + str(s.active))
        print("PREVIOUS DEC.:  " + str(s.previousDecision))
        print("PREVIOUS RAISE: " + str(s.previousRaise))
        print("PREVIOUS ALL M. " + str(s.previousSpentAll))
        print("IS RAISER:      " + str(s.raisePlayer))
        print("HAND:           " + str(s.hand))
        print("MIN Payment     " + str(minPayment))
        print("ALL PLAYERS \nMONEY IN ROUND: " + str(actualPot))
        print("--------------------------")









