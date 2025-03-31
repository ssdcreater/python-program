import random

def roll():
    n = random.randrange(1,7)
    return n

def bitten(currentPos):
    print("You are a BITTEN.")
    if currentPos == 38:
        return 5
    elif currentPos == 53:
        return 15
    elif currentPos == 96:
        return 67
    elif currentPos == 99:
        return 21
    
import random

#it change position from ladder-botton to ladder-top.

def roll():
    n = random.randrange(1,7)
    return n

def ladder(currentPos):
    print("You have got a LADDER.")
    if currentPos == 2:
        return 23
    elif currentPos == 7:
        return 49
    elif currentPos == 16:
        return 97
    elif currentPos == 41:
        return 63
    elif currentPos == 69:
        return 95

#cheak if the player is bitten by a snake.

def  isBitten(currentPos):
    if currentPos == 38 or currentPos ==  53 or currentPos == 96 or currentPos == 99:
        return True
    else:
        return False

#checks if the player has got ladder.

def gotLadder(currentPos):
    if currentPos == 2 or currentPos == 7 or currentPos == 16 or currentPos == 41  or currentPos == 69:
        return True
    else:
        return False

def play(n):
    nos = 0
    total = 0
    a = roll()
    if a == 6:
        while a ==6:
            nos += 1
            if nos >= 3:
                print("You have got 3 sixes.")
                total = 0
                break
            else:
                print("you have got a 6. You have got another turn.")
                total += 6
                a = roll()
            print("You have Got",total)
            n += a
        else:
            print("You have Got",a)
            n += total
    print("You reach",n)
    if isBitten(n) == True:
        n = bitten(n)
        print("You landed on",n)
    if gotLadder(n) == True:
          n = ladder(n)
          print("You got to",n)
    return n

def ready():
    a = roll()
    print("You have Got",a)
    if a == 1:
        print("You are ready to go ahead.Your current position is 1")
        return True


def gameOver():
    if p1 >=100 or p2 >= 100:
        print("GAME OVER")
        if p1 >= 100:
            print("PLAYER 1 win.")
        if p2 >= 100:
            print("PLAYER 2 win.")
            
        return True
    else:
        return False

p1 = 0
p2 = 0
isP1ready = False
isP2ready = False

print("here starts the game.please Roll.")
print("player1 yourcurrentposition is 0")
print("player2 yourcurrentposition is 0")

def player1():
    print("\t<<< Player 1 Turn >>>")
    global p1
    global isP1ready
    if isP1ready == False:
        if ready() == True:
            P1 = 1
            isP1ready = True
    else:
        p1 = play(p1)
          
def player2():
    print("\t<<< Player 2 Trurn >>>")
    global p2
    global isP2ready
    if isP2ready == False:
        if ready() == True:
            P2 = 1
            isP2ready = True
    else:
        p2 = play(p1)
        
while gameOver()==False:
    choice  = input()
    player1()
    player2()
    print()
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------------------------->>>>>>>>>>>>>>>>>>>>>")
    print()
    


     
    
    

  



    
    

  
