#!/usr/bin/env python
# coding: utf-8

# In[3]:


print ("Welcome to the Guessing Game Challenge")
print ("Rules: ")
print ("1. The Computer Picks a number in the range of 1 to 100 and only computer knows it")
print ("2. The Player has to guess a number and the following messages will be displayed according to the guess")
print ("3. If the number is within 10 of the number return 'WARM!'")
print ("4. If the number is further than 10 away from the number return 'COLD!'")
print ("5. If the number is closer than the previous guess then 'WARMER!'")
print ("6. If the number is farther than the previous guess then 'COLDER!'")


from random import randint
comp=randint(0,100)
print(" ")
l=list(range(1,100))
print(" ")
lg=[0]*100


#1st Guess
lg[0]=int (input ("Dear User Enter the First Guess"))
if abs(lg[0]-comp)>10:
    print("Cold")
elif abs(lg[0]-comp)<10 and abs(lg[0]-comp)>0:
    print("Warm")
elif lg[0]==comp:
    print(f"Congratulations! Found {comp} in 1st guess")


#From 2nd Guess Onwards
for i in l:
    lg[i]=int(input("Dear User Enter the Next Guess"))
    if lg[i]==comp:
        print (f"You Found the Number {comp} at Guess {i}" )
        break
    elif abs(lg[i]-comp) > abs(lg[i-1]-comp):
        print ("Colder")
    elif abs(lg[i]-comp)<abs(lg[i-1]-comp):
        print ("Warmer")
if i==100:
    print("Exhausted All Tries")


# 
