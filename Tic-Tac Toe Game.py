#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Known Bugs as of 15th April-NONE


# In[3]:


#Global Variables
grid = [[' _ ',' _ ',' _ '],[' _ ',' _ ',' _ '],[' _ ',' _ ',' _ ']]
turn=0
ch= ' '
import sys


# In[4]:


def welcome_screen():
    '''
    Function that Prints Welcome_Screen
    Parameters Required- None
    '''
    global turn
    turn=0
    print(' ')
    print (' ')
    print ("X X X Tic Tac Toe O O O")
    print (" ")
    print ("TicTacToe is a 2 player game, player 1 gets X and player 2 gets O as the symbol")
    print (" ")
    print ("The Rule is Simple! Get three continuous X's or O's to win!")
    print (" ")
    print ("For this version you've to enter the coordinate of the grid in which you'll enter your symbol")
    print ("for help a coordinated diagram of grid is given")
    print (" ")
    print ("      0       1       2")
    print (" ")
    print ("   0  _       _       _")
    print (" ")
    print ("   1  _       _       _")
    print (" ")
    print ("   2  _       _       _")
    print (" ")
    a= input("Press any key to Continue!")


# In[5]:


def inpu():
    '''
    Takes in entries of the symbols at said coordinate by the user, call fun welcome_screen() to get representation of 
    accessing the grid using coordinates
    
    Parameters required: None
    '''
    global turn
    global grid
    global ch
    co1=(0,0)
    co2=(0,0)
    if turn<=8:
        if turn%2==0:
            co1= input("Player1! Enter your desired coordinate in this ab form, a is row and b is column")
            if chec_dup(co1)==True:
                ch='X'              #NOT-DEFINED! CHECKS DUPLICATE ENTRY
                placesy('X',co1)
                
                
            else:
                print("Can't change already placed Symbol")
                inpu() #ERROR POSSIBLE
        else:                
            co2= input("Player2! Enter your desired coordinate in this ab form where a is row and b is column")
            if  chec_dup(co2)==True: #DEFINE A FUNCTION TO CHECK DUPLICATE ENTRY
                ch='O'
                placesy ('O',co2)
                
            else:
                print("Can't Change Already Placed Symbol")
                inpu() #ERROR POSSIBLE


# In[6]:


def placesy(ch,co):
    '''
    Assigns a symbol to the said index in the list
    Required Parameters: character 'X' or 'O' and index of the list in for ab for a-th row and b-th column
    '''
    x=int (co[0])
    y=int (co[1])
    grid[x][y]=' '+ch+' '
    print_fun()
    turnch()


# In[7]:


def turnch():
    '''
    Checks the count of turns taken
    Parameters: None
    '''
    global turn
    global ch
    while turn!=8:
        turn+=1
        if chec_win(grid,ch)==True and ch=='X':
            print ("Player 1 has won!")
        elif chec_win(grid,ch)==True and ch=='O':
            print ("Player 2 has won!")
        else:
            inpu()  
 
    if turn==8:
        if chec_win(grid,ch)==True and ch=='X':
            print ('Player 1 has won!')
        elif chec_win(grid,ch)==True and ch=='O':
            print ("Player 2 has won!")
        else:
            print ("Out of Turns! Resetting Board! Game Over")
        playagain()
        reset()


# In[8]:


def print_fun():
    '''
    Function that prints the board after each subsequent turns
    Parameter Required: None
    '''
    
    for i,j,k in grid:
        print ('     '+i+'   | ',end=' ')
        print ('     '+j+'   | ',end=' ')
        print ('     '+k+'   | ')


# In[9]:


def playagain():
    '''
    Checks if the user wants to play once again
    Parameter Required: None
    '''
    choice = input('Wanna Play Again? Y/N ')
    if choice=='Y':
        welcome_screen()
        reset()
        inpu()
    else:
        print("Thanks for Playing! Created by Tanay Shankar and Swati Sheenum!")
        sys.exit(0)


# In[10]:


def chec_win(check,c):
    '''
    Checks if one of the two players have won or not
    
    Parameters Required: grid list/board which is used to check if three continuous 'X' or 'O's have appeared on the board or not
    if true, sets turn variable to 8 to exhaust all turns
    '''
    global turn
    if   check[0][0]==check[1][1]==check[2][2]==' X ' or check[0][0]==check[1][1]==check[2][2]==' O ' :
        turn=8
        return True
    elif check[0][0]==check[1][0]==check[2][0]==' X ' or check[0][0]==check[1][0]==check[2][0]==' O ':
        turn=8
        return True
    elif check[0][1]==check[1][1]==check[2][1]==' X ' or check[0][1]==check[1][1]==check[2][1]==' O ' :
        turn=8
        return True
    elif check[0][2]==check[1][2]==check[2][2]==' X ' or check[0][2]==check[1][2]==check[2][2]==' O ':
        turn=8
        return True
    elif check[0][2]==check[1][1]==check[2][0]==' X ' or check[0][2]==check[1][1]==check[2][0]==' O ':
        turn=8
        return True
    elif check[2][0]==check[2][1]==check[2][2]==' X ' or check[2][0]==check[2][1]==check[2][2]==' O ':
        turn=8
        return True
    elif check[1][0]==check[1][1]==check[1][2]==' X ' or check[1][0]==check[1][1]==check[1][2]==' O ':
        turn=8
        return True
    elif check[0][0]==check[0][1]==check[0][2]==' X ' or check[0][0]==check[0][1]==check[0][2]==' O ':
        turn=8
        return True
    else:
        return False


# In[11]:


def reset():
    '''
    Resets the board and turn count when called
    
    Parameters: None
    '''
    global turn
    global grid
    grid = [[' _ ',' _ ',' _ '],[' _ ',' _ ',' _ '],[' _ ',' _ ',' _ ']]
    turn=0


# In[12]:


def chec_dup (check):
    '''
    checks if a duplicate entry has been made
    
    parameters: coordinates passed by a player
    '''
    a=int(check[0])
    b=int(check[1])
    global grid
    if grid[a][b]==' X ' or grid[a][b]==' O ':
        return False
    else:
        return True


# In[13]:


def begin():
    '''
    Starts the game
    '''
    reset()
    welcome_screen()
    inpu()


# In[24]:

begin()



# 2## 
