#!/usr/bin/env python
# coding: utf-8

# In[ ]:


cc=''
def inpu():
    global cc
    cc=input("Enter a 16 Digit Credit Number")
    checksum(cc)
def checkdig():
    '''
    Inputs a credit card number and checks if its 16 digits
    '''
    if len(cc)==16:
        return True
    else:
        return False
def checksum(cc):
    '''
    CheckSum Algorithm
    '''
    if checkdig()==True:
        su=0
        co=0
        nd=0
        cc1=cc[::-1]
        for ch in cc1:
            if co%2==1:
                nd=int(ch)*2
                if nd>=10:
                    su=su+int((nd/10))
                    su=su+(nd%10)

                else:
                    su=su+nd
            else:
                su=su+int(ch)
            co+=1
        if su%10==0:
            print("Credit Card is Valid")
        else:
            print("Credit is Invalid")
    else:
        print("Credit Card Invalid")
    again()
def again():
    ch=input("Another Credit Card to check? Y/N")
    if ch=='Y':
        global cc
        cc=''
        inpu()
    elif ch=='N':
        exit()
    else:
        print("Try Again!")
        again()
    
inpu()   

