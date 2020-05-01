#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Fibbonacci Series upto nth Term
#Program Overview:
#1. Series 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 .......
#2 Previous two terms are added and hence the first 2 numbers are fixed and printed at first
#3.Then C is printed which is a+b
#Then the term in b becomes term in a and term in c becomes term in b and same process is repeated

a=0
b=1
c=0
n=int(input("Enter limit"))
l=list(range(0,n))
print (a,',',b,end=', ')
for i in l:
    c=a+b
    a=b
    b=c
    print(c, end=', ')


# In[ ]:




