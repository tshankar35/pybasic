#!/usr/bin/env python
# coding: utf-8

# In[7]:


#----------------Prime Factorisation--------------------#
#Find and display Prime Factors 
#Takes a number finds its factors and checks which number is a prime number

l=[]
def inpt():
    global l
    nu=int(input("Enter a number to finds its prime factors"))
    lister=list(range(1,nu+1))
    for i in lister:
        if nu%i==0:
            l.append(i)
    l=set(l)
    l=list(l)
    print(l)
    primefactr()
def primefactr():
    global l
    c1=0
    for k in l:
        lister_2=list(range(1,k+1))
        count=0
        for j in lister_2:
            if k%j==0:
                count+=1
                c1+=1
        if count==2:
            print(j)
            continue
    l=[]

inpt()    


# In[6]:





# In[ ]:




