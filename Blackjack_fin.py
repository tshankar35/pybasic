#!/usr/bin/env python
# coding: utf-8

# In[1]:


lista=["Spades","Diamonds","Clubs","Hearts"]
listb=["King","Queen","Jack","Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
corresp={"Ace":11,"King":10,"Queen":10,"Jack":10,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9}
listpc=[]
card=' '
valhc=0
holec=" "
sumdc=0
sumpc=0
acc=5000
wager=0


# In[2]:


def rules():
    '''
    A function that prints the rules of game
    '''
    print ("___________------------------BlackJack-----------------____________")
    print (" ")
    print ("Welcome to the game of Blackjack!")
    print ("The Rule is simple! Draw cards as close to a sum of 21 and that sum is greater than that of the dealer")
    print ("If the dealer or the player goes over 21 during their turn, they bust!")
    print ("King, Queen and Jacks are each treated as a card of value 10")
    print ("Aces are treated as a card of value 1 or 11, depending on player's choice")
    print ("Other cards are treated according to their face value")
    print ("Player gets an initial account balance of $5000")
    print (' ')
    a= input("So are you ready? Press Enter to continue")


# In[3]:


import random
class Deck():
    global lista
    global listb
    global corresp
    #Defines Deck
    def __init__(self):
        print ("Random Card Drawn!")
        
    def playerdec():
        global card
        val1=0
        a=random.randint(0,3)
        b=random.randint(0,11)
        card=listb[b]+" of "+lista[a]
        val1 = corresp.get(listb[b])
        return val1
    


# In[4]:


def playercards():
        print ("For Player")
        global sumpc
        vala=0
        valb=0
        card1str=' '
        card2str=' '
        global card
        card1=Deck()
        vala=Deck.playerdec()
        print (f"{card} = {vala}")
        card1str=card
        card2=Deck()
        valb=Deck.playerdec()
        print (f"{card} = {valb}")
        card2str=card
        if vala==11 and vala+valb>21:
            vala=1
            print ("Ace chosen as 1")
        elif valb==11 and vala+valb>21:
            valb=1
            print ("Ace chosen as 1")
        sumpc=vala+valb
        print (sumpc)


# In[5]:


def dealer():
    print ("For Dealer")
    global sumdc
    vala=0
    global valhc
    global holec
    card1str=' '
    global card
    card1=Deck()
    vala=Deck.playerdec()
    print (f"{card} = {vala}")
    card1str=card
    card2=Deck()
    valhc=Deck.playerdec()
    holec=card
    if vala==11 and vala+valhc>21:
            vala=1
    elif valhc==11 and vala+valhc>21:
            valhc=1
    sumdc=vala+valhc


# In[6]:


def hitd():
    sumoc=0
    global card
    global sumdc
    global sumpc
    cardhit=Deck()
    cardval=Deck.playerdec()
    if cardval==11 and (sumdc+cardval>21): 
        cardval=1
    print (f"{card} = {cardval}")
    sumoc=sumoc+cardval
    return sumoc


# In[7]:


def hitp():
    sumoc=0
    global card
    global sumdc
    global sumpc
    cardhit=Deck()
    cardval=Deck.playerdec()
    if cardval==11 and (sumpc+cardval>21): 
        cardval=1
    print (f"{card} = {cardval}")
    sumoc=sumoc+cardval
    return sumoc


# In[8]:


def logix():
    global sumpc
    global sumdc
    global holec
    global valhc
    global acc
    global wager
    if sumpc==21:
        print ("BlackJack! You win")
        acc=acc+(wager*2)
        print(f"Player has now currently ${acc} and has won additional ${wager}")
        print (" ")
    else:  
        print (f"Player has drawn a card of sum {sumpc}")
        
        while True:
            
            choice = input ("Hit or Stand? ")
            if choice=='Hit' or choice=="Hit Me":
                sumpc = sumpc+hitp()
                print(f"New Sum {sumpc}")
                if sumpc==21:
                    print ("Turn Over")
                    continue
                elif sumpc<21:
                    continue
                elif sumpc>21:
                    print ("BUST! House Wins")
                    print(f"Player has now currently ${acc} and has lost ${wager}")
                    break
                
            elif choice=="Stand":
                print (f"Player's new total {sumpc}")
                print (f"Dealer's Hole Card is {holec} whose value is {valhc}")
                print (f"Current Sum of Dealer is {sumdc}")
                while True:
                    if  sumdc<17:
                
                        print ("Dealer has decided to Hit")
                        sumdc=sumdc+hitd()
                        print (f"New Sum {sumdc}")
                        continue
                    elif sumdc>=17 and sumdc<21:
                        r=random.randint(0,10)
                        if r==0 and sumdc!=sumpc:
                    
                            print ("Dealer decided to Hit")
                            sumdc=sumdc+hitd()
                            print (f"New Sum {sumdc}")
                            continue
                        else:
                            print ("Dealer Decides to Stand")
                            break
                    elif sumdc>21:
                        
                        print ("Dealer Busted! Player Wins")
                        acc=acc+(wager*2)
                        print(f"Player has now currently ${acc} and has won additional ${wager}")
                        break
                    
                    elif sumdc==21:
                        if sumpc==21:
                            print ("Push! No One wins")
                            acc=acc+wager
                            print(f"Player has now currently ${acc} and has received back the wager")
                            break
                        else:
                            print (f"New Sum of Player's Cards {sumpc}")
                            print ("House Wins")
                            print (f"Player has now currently ${acc} and has lost ${wager}")
                            break
                    
            break
                             
                   
                
        if sumdc<=21 and sumpc<=21 and sumdc>sumpc:
            
            print ("House Wins")
            print(f"Player has now currently ${acc} and has lost ${wager}")
            
        elif sumdc<=21 and sumpc<=21 and sumdc<sumpc:
            
            print ("Player Wins")
            acc=acc+(wager*2)
            print(f"Player has now currently ${acc} and has won additional ${wager}")
           
                
        elif sumdc<=21 and sumpc<=21 and sumdc==sumpc:
            print ("Push! No one Wins")
            acc=acc+wager
            print(f"Player has now currently ${acc} and has received back his wager")
            
    


# In[9]:


def Account():
    global wager
    global acc
    print (f"You have ${acc}")
    wager=int (input("Enter Wager: "))
    if wager>acc:
        print ("Insufficient Balance")
        Account()
    else:
        acc = acc-wager
    print (f"At present you have ${acc} and you've placed a wager of ${wager}")
    print (" ")


# In[10]:


def letsplay():
    global acc
    acc=5000
    rules()
    Account()
    playercards()
    dealer()
    logix()
    playagain()
    print (" ")
def reset():
    global card
    global valhc
    global holec
    global sumdc
    global sumpc
    global wager
    card=' '
    valhc=0
    holec=" "
    sumdc=0
    sumpc=0
    wager=0
def playagain():
    while True:
        ch=input("Wanna Play Again? Y/N?")
        print (" ")
        if ch=='Y':
            reset()
            playercards()
            dealer()
            Account()
            logix()
            continue
        elif ch=='N':
            
            print ("Thanks for playing! By Tanay Shankar")
            break
        else:
            print ("Unidentifiable entry! Try Again")
            continue


# In[12]:


letsplay()


# In[ ]:




