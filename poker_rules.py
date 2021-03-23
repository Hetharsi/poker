from itertools import permutations
from functools import reduce
import poker



cards = [('sz', 2), ('k', 2),('t', 2),('p', 2), ('sz', 3), ('k', 3),('t', 3),('p', 3), ('sz', 4), ('k', 4),('t', 4),('p', 4), ('sz', 5), ('k', 5),('t', 5),('p', 5),('sz', 6), ('k', 6),('t', 6),('p', 6), ('sz', 7), ('k', 7),('t', 7),('p', 7), ('sz', 8), ('k', 8),('t', 8),('p', 8), ('sz', 9), ('k', 9),('t', 9),('p', 9), ('sz', 10), ('k',10),('t', 10),('p', 10), ('sz', 11), ('k',11),('t', 11),('p', 11), ('sz', 12), ('k',12),('t', 12),('p', 12), ('sz', 13), ('k',13),('t', 13),('p', 13),('sz', 14), ('k',14),('t', 14),('p', 14)]



def findBestHand(hand):
    if isFlush(hand):
        return (10, best_flush(hand))
    elif isPoker(hand):
        return (9, best_poker(hand))
    elif isFull(hand):
        return (8, best_full(hand))
    elif isPoker(hand):
        return (7 ,best_poker(hand))
    elif isFull(hand):
        return (6, best_full(hand))
    elif isColourFlush(hand):
        return (5, best_colour_flush(hand))
    elif isStraight(hand):
        return (4, best_straight(hand))
    elif isDrill(hand):
        return (3, best_drill(hand))
    elif is_twoPair(hand): 
        return (2, best_twoPair(hand))
    elif isPair(hand):
        return (1, best_pair(hand))
    else: 
        return (0, emptyHand(hand))
'''Return 

'''
def isPoker(hand):
    boolean_poker = False
    hand = list(map (lambda x: x[1], hand))
    setHand = sorted(list(set(hand)))
    countedCards = ()
    for i in setHand:
        countedCards += ((i, hand.count(i)), )
    for x in countedCards:
        if x[1] == 4: boolean_poker = True
    return boolean_poker
def best_poker(hand):
    if isPoker(hand):
        hand = list(map (lambda x: x[1], hand))
        setHand = sorted(list(set(hand)))
        myTuple = ()
        for i in setHand:
            myTuple += ((i, hand.count(i)),)
        bestTuple = myTuple[0]
        for x in myTuple:
            if x[1] > bestTuple[1]:
                bestTuple = x
            elif(x[1] == bestTuple[1] and x[0]>bestTuple[0]):
                bestTuple = x
        if bestTuple[1] == 4: return(bestTuple)
    else: return ("Not poker")
def isFull(hand):
    isFull = False
    if isPair(hand) == True and isDrill(hand) == True:
        isFull = True
    return (isFull)
def best_full(hand):
    if isFull(hand):
        bestFull = (best_drill(hand), ) + (best_pair(hand), )
    return bestFull
def isPair(hand):
    isPair = False
    hand = list(map (lambda x: x[1], hand))
    myTuple = ()
    setHand = sorted(list(set(hand)))
    for i in setHand:
        myTuple += ((i, hand.count(i)),)
    for x in myTuple:
        if x[1] == 2: isPair = True
    return(isPair)
def isDrill(hand):
    isDrill = False
    hand = list(map (lambda x: x[1], hand))
    myTuple = ()
    setHand = sorted(list(set(hand)))
    for i in setHand:
        myTuple += ((i, hand.count(i)),)
    for x in myTuple:
        if x[1] == 3: isDrill = True
    return(isDrill)
def best_drill(hand):
    bestDrill = ()
    if isDrill(hand) == True:
        hand = list(map (lambda x: x[1], hand))
        setHand = sorted(list(set(hand)))
        myTuple = ()
        for i in setHand:
            myTuple += ((i, hand.count(i)),)
        bestTuples = tuple(filter((lambda x: x[1] == 3), myTuple))
        bestDrill = bestTuples[0]
        for x in bestTuples:
            if(x[0]>bestDrill[0]):
                bestDrill = x
        return(bestDrill)
def best_pair(hand):
    bestPair = ()
    if isPair(hand) == True:
        hand = list(map (lambda x: x[1], hand))
        setHand = sorted(list(set(hand)))
        myTuple = ()
        for i in setHand:
            myTuple += ((i, hand.count(i)),)
        bestTuples = tuple(filter((lambda x: x[1] == 2), myTuple))
        bestPair = bestTuples[0]
        for x in bestTuples:
            if(x[0]>bestPair[0]):
                bestPair = x
        return bestPair
def is_twoPair(hand):
    is2Pair = False
    a = 0
    hand = list(map (lambda x: x[1], hand))
    myTuple = ()
    setHand = sorted(list(set(hand)))
    for i in setHand:
        myTuple += ((i, hand.count(i)),)
    for x in myTuple:
        if x[1] == 2:
            a+= 1
            if a == 2: is2Pair = True
    return(is2Pair)
def best_twoPair(hand):
    best2Pair = ()
    if is_twoPair(hand):
        hand = list(map (lambda x: x[1], hand))
        setHand = sorted(list(set(hand)))
        myTuple = ()
        for i in setHand:
            myTuple += ((i, hand.count(i)),)
        bestTuples = tuple(filter((lambda x: x[1] == 2), myTuple))
        smallestPair = bestTuples[0]
        for x in bestTuples:
            if(x[0]<smallestPair[0]):
                smallestPair = x
        best2Pair = tuple(filter(lambda x: x != smallestPair, bestTuples))
        return(best2Pair)
def isColourFlush(hand):
    is_colour_flush = False
    hand = list(map (lambda x: x[0], hand))
    myTuple = ()
    setHand = sorted(list(set(hand)))
    for i in setHand:
        myTuple += ((i, hand.count(i)),)
    for x in myTuple:
        if x[1] > 4: is_colour_flush = True
    return (is_colour_flush)
def best_colour_flush(hand):
    bestColourFlush = ()
    if isColourFlush(hand):
        hand = list(map (lambda x: x[0], hand))
        myTuple = ()
        setHand = sorted(list(set(hand)))
        for i in setHand:
            myTuple += ((i, hand.count(i)),)
        for x in myTuple:
            if x[1] > 4:
                bestColourFlush = x
        return bestColourFlush
def help_straight(x, y):
    if sum(x) > sum(y):return x
    else: return y
def isFlush(hand):
    is_flush = False
    x = best_colour_flush(hand)
    if x == None: return is_flush
    y = list((filter(lambda a: x[0]==a[0], hand)))
    if isStraight(y): is_flush = True
    return is_flush
def best_flush(hand):
    if isFlush(hand):
        x = best_colour_flush(hand)
        y = list((filter(lambda a: x[0]==a[0], hand)))
        z = best_straight(y)
        return(z)
def isStraight(hand):
    boolean_straight = False
    hand = sorted(list(map (lambda x: x[1], hand)))
    hands = list(permutations(hand, 5))
    for x in hands:
        miniRound = True
        for i in range(0, len(x)-1):
            if x[i]+1 != x[i+1]: miniRound = False
        if miniRound == True:
            boolean_straight = True
    return(boolean_straight)
def best_straight(hand):
    straight = []
    straights = []
    hand = sorted(list(map (lambda x: x[1], hand)))
    hands = list(permutations(hand, 5))
    for x in hands:
        miniRound = True
        for i in range(0, len(x)-1):
            if x[i]+1 != x[i+1]: miniRound = False
        if miniRound == True:
            straights += [list(x)]
    straight = reduce((lambda x, y: help_straight(x, y)), straights)
    return(straight)
def emptyHand(hand): 
    return(hand)


