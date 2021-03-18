import player
import random
deck = [('sz', 2), ('k', 2),('t', 2),('p', 2), ('sz', 3),
        ('k', 3),('t', 3),('p', 3), ('sz', 4), ('k', 4),
        ('t', 4),('p', 4), ('sz', 5), ('k', 5),('t', 5),
        ('p', 5),('sz', 6), ('k', 6),('t', 6),('p', 6),
        ('sz', 7), ('k', 7),('t', 7),('p', 7), ('sz', 8),
        ('k', 8),('t', 8),('p', 8), ('sz', 9), ('k', 9),
        ('t', 9),('p', 9), ('sz', 10), ('k',10),('t', 10),
        ('p', 10), ('sz', 11), ('k',11),('t', 11),('p', 11),
        ('sz', 12), ('k',12),('t', 12),('p', 12), ('sz', 13),
        ('k',13),('t', 13),('p', 13),('sz', 14), ('k',14),('t', 14),('p', 14)]

def make_players_active(players)-> [player]:
    activePlayers = []
    for player in players:
        if player.inGame == True and player.inRound == True:
            activePlayers += [player]
    return activePlayers
def make_players() -> [player]:
    #players_n = int(input("How many players are in the game?"))
    players_n = 3
    players = []
    for i in range(0, players_n):
        players += [player.Player(f"Player {i}", int(i))]
    return players
def make_playersActive(players)-> [player]:
    for x in players:
        x.active = True
    return players

def draw1Card(players, deck)->[player]:
    newCard = []
    newCard += [deck.pop(random.randint(0, len(deck)-1))]
    for x in players:
        x.hand += newCard
    return players
def draw2Cards(players, deck:tuple)-> [player]:
    for i in range (2):
        for x in players:
            x.draw_card(deck)
    return players
def draw3Cards(players, deck)->[player]:
    newCards = []
    newCards += [deck.pop(random.randint(0, len(deck)-1))]
    newCards += [deck.pop(random.randint(0, len(deck)-1))]
    newCards += [deck.pop(random.randint(0, len(deck)-1))]
    for x in players:
        x.hand += newCards


def playersInformation(players, actualPot:int)->None:
    global minPayment
    for x in players:
        x.playerInformation(actualPot, minPayment)
def showBeforePlayerTurn(player, minPayment, actualPot)->None:
    print(str(player.name) + "']s this is your turn!")
    print("This is the money in the pool: " + str(actualPot))
    print("Your money: " + str(player.money))
    print("Minimum payment: "  +str(minPayment))
    print("This is your hand: " + str(player.hand))

def playerDecision(player)-> int:
    global minPayment, actualPot
    showBeforePlayerTurn(player, minPayment, actualPot)
    answer = input("What do you want to do? \n1: pass\n2: Throw your hand\n3: Raise money: \n4: Keep pot:\n ")
    if (answer == "1") and (minPayment == 0): player.passTurn(actualPot, minPayment)
    elif answer == "2":
        player.throwHand()
    elif answer == "3":
        actualPot = player.raise_pot(actualPot, minPayment)
        minPayment = player.moneyInRound
    elif answer == "4":
        actualPot = player.keepPot(actualPot, minPayment)
    else: print("asdf" + actualPot)
    return actualPot
def playerDecisionWith2Cards(player)->str:
    global roundPot, minPayment
    print("The best hand for you is:", end= "")
    print(player.getBestHand())
    if player.previousDecision == "3" and player.raisePlayer == True:
        minPayment = 0
    elif player.previousDecision == "3":
        minPayment -= player.previousSpentAll


    player.playerInformation(roundPot, minPayment)
    answer = input("What do you want to do? \n2: Throw your hand\n3: Raise money: \n4: Keep pot:\n ")

    if answer == "2":
        player.throwHand()
    elif answer == "3":
        minPayment = player.raise_pot(roundPot, minPayment)
        roundPot += minPayment
    elif answer == "4":
        minPayment = player.keepPot(roundPot, minPayment)
        roundPot += minPayment
    return answer

def countPassiveRoundPlayers(inRoundPlayers)-> int:
    passivePlayers = len(inRoundPlayers)
    for x in inRoundPlayers:
        if x.active == False: passivePlayers -= 1
    return passivePlayers
def inRoundOnly1Player(players)-> bool:
    activePlayers = 0
    for x in players:
        if x.active == True:
            activePlayers += 1
    if activePlayers == 1:
        return True
    else: return False

def allNonActive(players)-> bool:
    result = True
    for x in players:
        if x.active == True: result = False
    return result
def roundWinner(players)-> player:
    #Not in all cases will this return player
    for x in players:
        if x.active == True:
         return x

def playersOrder(players)->[player]:
    newOrder = []
    for i in range(1, (len(players))):
        newOrder += [players[i]]
    newOrder += [players[0]]
    return newOrder
def set_roundPlayers_default(players)-> [player]:
    for p in players:
       p.active = True
       p.inRound = True
       p.raisePlayer = False
       p.previousDecision = "No decisision yet"
       p.previousRaise = 0
    return players
def endOfGame(players)->bool:
    global roundPot
    if len(players) <= 1:
        players[0].money += roundPot
        return True
    else: return False


#Always make the game with 5 players
if __name__ == "__main__":
    players           = make_players()
    activeGamePlayers = make_players_active(players)
    inactivePlayers   = []

    while(endOfGame(activeGamePlayers) != True):
        minPayment = 50
        roundPot = 0
        roundPlayers = activeGamePlayers
        ind = 0

        #draw 2   cards
        draw2Cards(roundPlayers, deck)

        while(len(roundPlayers)!= 1 and countPassiveRoundPlayers(roundPlayers) != 0):
            if ind > len(roundPlayers)-1:
                ind = 0
            ans = playerDecisionWith2Cards(roundPlayers[ind])
            if "2" == ans:
                inactivePlayers += [roundPlayers.pop(ind)]
                continue
            elif "3" == ans:
                for p in roundPlayers:
                    if roundPlayers[ind].name != p.name:
                        p.raisePlayer=False
            ind += 1


        print("in the end ============== player")
        playersInformation(players, 0)
        print("in the end ============== roundPlayer")
        playersInformation(roundPlayers, 0)

        if endOfGame(roundPlayers) == True:
            print("This game was won by " + str(roundPlayers[0].name))
            continue

        #draw 3 cards
        set_roundPlayers_default(roundPlayers)
        ind = 0
        minPayment = 0
        draw3Cards(roundPlayers, deck)
        while(len(roundPlayers)!= 1 and countPassiveRoundPlayers(roundPlayers) != 0):
            if ind > len(roundPlayers)-1:
                ind = 0
            ans = playerDecisionWith2Cards(roundPlayers[ind])
            if "2" == ans:
                inactivePlayers += [roundPlayers.pop(ind)]
                continue
            elif "3" == ans:
                for p in roundPlayers:
                    if roundPlayers[ind].name != p.name:
                        p.raisePlayer=False
            ind += 1

        print("in the end ============== roundPlayer")
        playersInformation(roundPlayers, 0)

        #draw 1 card
        set_roundPlayers_default(roundPlayers)
        ind = 0
        minPayment = 0
        draw1Card(roundPlayers, deck)
        while(len(roundPlayers)!= 1 and countPassiveRoundPlayers(roundPlayers) != 0):
            if ind > len(roundPlayers)-1:
                ind = 0
            ans = playerDecisionWith2Cards(roundPlayers[ind])
            if "2" == ans:
                inactivePlayers += [roundPlayers.pop(ind)]
                continue
            elif "3" == ans:
                for p in roundPlayers:
                    if roundPlayers[ind].name != p.name:
                        p.raisePlayer=False
            ind += 1

        print("in the end ============== roundPlayer")
        playersInformation(roundPlayers, 0)

        #draw 1 card
        set_roundPlayers_default(roundPlayers)
        ind = 0
        minPayment = 0
        draw1Card(roundPlayers, deck)
        while(len(roundPlayers)!= 1 and countPassiveRoundPlayers(roundPlayers) != 0):
            if ind > len(roundPlayers)-1:
                ind = 0
            ans = playerDecisionWith2Cards(roundPlayers[ind])
            if "2" == ans:
                inactivePlayers += [roundPlayers.pop(ind)]
                continue
            elif "3" == ans:
                for p in roundPlayers:
                    if roundPlayers[ind].name != p.name:
                        p.raisePlayer=False
            ind += 1

        print("in the end ============== roundPlayer")
        playersInformation(roundPlayers, 0)



