import copy
import random
VIC=10**20 #The value of a winning board (for max) 
LOSS=-VIC #The value of a losing board (for max)
TIE=0 #The value of a tie
SIZE=3 #The length of a winning sequence
COMPUTER=SIZE+1 #Marks the computer's cells on the board
HUMAN=1 #Marks the human cells on the board

'''
The HUMAN can select any number along a horizontal row that the cursor is on
The COMPUTER can select any number along a vertical row that the cursor is on
The state of the game is represented by a list of 4 items:
0. The game board - a matrix (list of lists) of ints. Empty cells = None,
   the comp's cells = COMPUTER and the human's = HUMAN
1. Computer's points
2. Human's points
3. Who's turn is it: HUMAN or COMPUTER
4. Next row/col
'''
def create(n):
    board=[] #The board is represented by a list of lists
    for i in range(n):
        board+= [[0]*n] #Add an empty row
    for j in board:
        for k in range(len(j)):
            j[k]=random.randint(-10, 10)
    print("board",board)
    return [board,0,0,COMPUTER,0] #The starting state of the game

def value(s):
#Returns the heuristic value of s
    if isFinished(s):
        if s[1]>s[2]:
            return VIC
        elif s[1]<s[2]:
            return LOSS
        else:
            return TIE
    else:
        if s[1]==s[2]:
            return 1/VIC
        return s[1]-s[2]




def printState(s):
#Prints the board. 
#If the game ended, prints who won.
    print(" "*6,end="")
    for c in range(len(s[0])):
        print(" "*(5-len(str(c))),c,end="")
    print("")
    for r in range(len(s[0])):
        print(r,"-"," "*(3-len(str(r))),end="")
        for c in range(len(s[0])):
            print(" "*(5-len(str(s[0][r][c]))),s[0][r][c],end="")
        print("")
    print("COMPUTER=",s[1]," HUMAN=",s[2])
    print("Take from row ",s[4])
    if value(s)==VIC:
        print("Ha ha ha I won!")
    elif value(s)==LOSS:
        print("You did it!")
    elif value(s)==TIE:
        print("It's a TIE")

def isFinished(s):
#Returns True iff the game ended
    if s[3]==HUMAN:
        for i in range(len(s[0])):
           if s[0][s[4]][i] is not None:
               return False
        return True
    else:
        for i in range(len(s[0])):
           if s[0][i][s[4]] is not None:
               return False
        return True
    
def isHumTurn(s):
#Returns True iff it the human's turn to play
    return s[3]==HUMAN

def whoIsFirst(s):
#The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you. : "))==1:
        s[3]=COMPUTER
    else:
        s[3]=HUMAN

def makeMove(s,r,c):
# Takes the Value in r,c and put None instead
# switches turns
# Assumes the move is legal.
    if s[3]==HUMAN:
        s[2]+=s[0][r][c]
        s[4]=c
    else:
        s[1]+=s[0][r][c]
        s[4]=r
    s[0][r][c]=None # marks the board
    s[3]=COMPUTER+HUMAN-s[3] # switches turns
   
def inputMove(s):
# Reads, enforces legality and executes the user's move.
    printState(s)
    flag=True
    while flag:
        move=int(input("Enter your next move: "))
        if move<0 or move>=len(s[0]) or s[0][s[4]][move] is None:
            print("Illegal move.")
        else:
            flag=False
            makeMove(s,s[4],move)
        
def getNext(s):
# returns a list of the next states of s
    ns=[]
    if s[3]==HUMAN:
        for i in range(len(s[0])):
            if s[0][s[4]][i] is not None:
                tmp=copy.deepcopy(s)
                makeMove(tmp,s[4],i)
                ns+=[tmp]
    else:
        for i in range(len(s[0])):
            if s[0][i][s[4]] is not None:
                tmp=copy.deepcopy(s)
                makeMove(tmp,i,s[4])
                ns+=[tmp]
    ns.sort(key=compPoints)
    return ns
    
def compPoints(s):
    return s[1]
