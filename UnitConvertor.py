#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Unit Convertor is a simple program that converts quantities such as temperature, currency, volume, mass, distance.
#User will input the value along with the unit in the pattern "x units". Do note that the space between the x and units is essential.
#The inputted unit has to be its representative letter. The compiler will have the ability to identify any of the such made inputs
#______________________________-----Program Framework-----__________________________"
# 1. User inputs --> x units
# 2. Compiler returns the said quantity inputted
# 3. Then gives the option to convert it into the available units (as a menu) and user selects the option
# 4. The conversion is made and displayed

x=' '
unit=' '
val=0.0
def inpu():
    global x
    x=input("Enter a quantity in form 'x units' :  ")
    unitfind()

import re
mass=['kg','g','mg','ug','pound','tonnes']
volume=['cm3','m3','L','l','mL','ml','ounce','oz']
currency=['$','Rs.','Rs','Euro','E','pounds','Yen','Y','Dollars']
temperature=['K','k','*C','C','F']
distance=['um','mm','cm','m','km','miles']

def unitfind():
    global x
    global val
    global unit
    found=''
    lister=list(x.split(' '))
    val=float(lister[0])
    unit=lister[1]
    for unit in mass:
        if unit==lister[1]:
                print("Mass unit")
                massconv()
    for unit in volume:
        if unit==lister[1]:
                print("Volume unit")
                volconv()
    for unit in temperature:
        if unit==lister[1]:
                print("Temperature unit")
                tempconv()
    for unit in distance:
        if unit==lister[1]:
                print ("Distance unit")
                distconv()

                
def massconv():
    global val
    global unit
    global mass
    print (f"{val} {unit}")
    i=1
    for units in mass:
        print (f"press {i} to convert {unit} to {units}")
        i+=1
    ch=int(input("Enter choice: "))
    if ch==1 and unit=='kg':
        print("Already in kg")
    elif ch==2 and unit=='g':
        print ("Already in g")
    elif ch==3 and unit=='mg':
        print ("Already in mg")
    elif ch==4 and unit=='ug':
        print ("ug")
    elif ch==5 and unit=='pound':
        print ("Already in pound")
    elif ch==6 and unit=='tonnes':
        print("Already in tonnes")
    elif ch==1:
        if unit=='g':
            val = val/1000
        if unit=='mg':
            val = val/1000000
        if unit=='ug':
            val=val/1000000000
        if unit=='pound':
            val=val/2.205
        if unit=='tonnes':
            val=val*1000
    elif ch==2:
        if unit=='kg':
            val = val*1000
        if unit=='mg':
            val = val/1000
        if unit=='ug':
            val=val/1000000
        if unit=='pound':
            val=val*454
        if unit=='tonnes':
            val=val*1000000
    elif ch==3:
        if unit=='kg':
            val = val * 1000000
        if unit=='g':
            val = val*1000
        if unit=='ug':
            val=val/1000
        if unit=='pound':
            val=val*453592
        if unit=='tonnes':
            val=val*1000000000
    elif ch==4:
        if unit=='kg':
            val = val * 1000000000
        if unit=='g':
            val = val*1000000
        if unit=='mg':
            val=val*1000
        if unit=='pound':
            val=val*453600000
        if unit=='tonnes':
            val=val*1000000000000
    elif ch==5:
        if unit=='kg':
            val = val * 2.205
        if unit=='g':
            val = val/454
        if unit=='ug':
            val=val/453600000
        if unit=='mg':
            val=val/453592
        if unit=='tonnes':
            val=val*2204.62
    elif ch==6:
        if unit=='kg':
            val = val / 1000
        if unit=='g':
            val = val/1000000
        if unit=='ug':
            val=val/1000000000000
        if unit=='pound':
            val=val/2205
        if unit=='mg':
            val=val/1000000000
            
    print(f"{val} {mass[ch-1]}")   
    again()
    

def volconv():
    global val
    global unit
    vol1=['cm3','m3','L','mL','oz']
    print (f"{val} {unit}")
    i=1
    for units in vol1:
        print (f"press {i} to convert {unit} to {units}")
        i+=1
    ch=int(input("Enter choice: "))
    if ch==1 and unit=='cm3':
        print("Already in cm3")
    elif ch==2 and unit=='m3':
        print ("Already in m3")
    elif ch==3 and (unit=='L' or unit=='l'):
        print ("Already in L")
    elif ch==4 and (unit=='mL' or unit=='ml'):
        print ("Already in mL")
    elif ch==5 and (unit=='oz' or unit =='ounces'):
        print ("Already in ounces")
    elif ch==1:
        if unit == 'm3':
            val = val*1000000
        if unit == 'L' or unit == 'l':
            val = val* 1000
        if unit == 'mL' or unit == 'ml':
            val = val
        if unit == 'oz' or unit =='ounces':
            val = val * 29.574
    elif ch==2:
        if unit == 'cm3':
            val = val / 1000000
        if unit == 'L' or unit == 'l':
            val = val / 1000
        if unit == 'mL' or unit == 'ml':
            val = val / 1000000
        if unit == 'oz' or unit =='ounces':
            val = val / 33814
    elif ch==3:
        if unit == 'cm3':
            val = val / 1000
        if unit == 'm3':
            val = val * 1000
        if unit == 'mL' or unit == 'ml':
            val = val / 1000
        if unit == 'oz' or unit =='ounces':
            val = val / 33.814
    elif ch==4:
        if unit == 'cm3':
            val = val 
        if unit == 'm3':
            val = val * 1000000
        if unit == 'l' or unit == 'L':
            val = val * 1000
        if unit == 'oz' or unit =='ounce':
            val = val * 29.574
    elif ch==5:
        if unit == 'cm3':
            val = val / 29.574
        if unit == 'm3':
            val = val * 33814
        if unit == 'l' or unit == 'L':
            val = val * 33.814
        if unit == 'ml' or unit =='mL':
            val = val / 29.574
    print(f"{val} {vol1[ch-1]}")
    again()
    
    
    
def tempconv():
    global val
    global unit
    temp = ['K','C','F']
    print (f"{val} {unit}")
    i=1
    for units in temp:
        print (f"press {i} to convert {unit} to {units}")
        i+=1
    ch=int(input("Enter choice: "))
    if ch==1 and (unit=='K' or unit=='k'):
        print("Already in Kelvin")
    elif ch==2 and (unit=='C' or unit=='*C'):
        print ("Already in Celcius")
    elif ch==3 and unit=='F':
        print ("Already in Fahrenheit")
    elif ch==1:
        if unit == 'C' or unit =='*C':
            val = val+273.15
        if unit == 'F':
            val = ((val-32)/(5/9))+273.15
    elif ch==2:
        if unit == 'K' or unit =='k':
            val = val-273.15
        if unit == 'F':
            val = ((val-32) * (5/9))
    elif ch==3:
        if unit == 'C' or unit =='*C':
            val = (val*(9/5))+32
        if unit == 'K' or unit =='k':
            val = ((val-273.15)*(9/5))+32
    print(f"{val} {temp[ch-1]}")
    again()
    
    
def distconv():
    global val
    global unit
    global distance
    
    print (f"{val} {unit}")
    i=1
    for units in distance:
        print (f"press {i} to convert {unit} to {units}")
        i+=1
    ch=int(input("Enter choice: "))
    if ch==1 and unit=='um':
        print("Already in micrometer")
    elif ch==2 and unit=='mm':
        print ("Already in millimeter")
    elif ch==3 and unit=='cm':
        print ("Already in centimeter")
    elif ch==4 and unit=='m':
        print ("Already in meter")
    elif ch==5 and unit=='km':
        print ("Already in kilometer")
    elif ch==6 and unit=='miles':
        print("Already in miles")
    elif ch==1: #to um
        if unit=='mm':
            val = val*1000
        if unit=='cm':
            val = val*10000
        if unit=='m':
            val=val*1000000
        if unit=='km':
            val=val*1000000000
        if unit=='miles':
            val=val*1609000000
    elif ch==2: # to mm
        if unit=='um':
            val = val/1000
        if unit=='cm':
            val = val*10
        if unit=='m':
            val=val*1000
        if unit=='km':
            val=val*1000000
        if unit=='miles':
            val=val*1609000
    
    elif ch==3: # to cm
        if unit=='um':
            val = val / 10000
        if unit=='mm':
            val = val / 10
        if unit=='m':
            val=val * 100
        if unit=='km':
            val=val*100000
        if unit=='miles':
            val=val*160934
    
    elif ch==4:# to m
        if unit=='um':
            val = val / 1000000
        if unit=='mm':
            val = val / 1000
        if unit=='cm':
            val=val / 100
        if unit=='km':
            val=val * 1000
        if unit=='miles':
            val=val*1609
    elif ch==5: # to km
        if unit=='um':
            val = val / 1000000000
        if unit=='mm':
            val = val / 1000000
        if unit=='cm':
            val=val / 100000
        if unit=='m':
            val=val/1000
        if unit=='miles':
            val=val*1.609
    elif ch==6: # to miles
        if unit=='um':
            val = val / 1609000000
        if unit=='mm':
            val = val/1609000
        if unit=='cm':
            val=val/160934
        if unit=='m':
            val=val/1609
        if unit=='km':
            val=val/1.609
    print(f"{val} {distance[ch-1]}")   
    again()

def again():
    ch=input("Again? Y/N ")
    if ch=='Y':
        global x
        global unit
        global val
        x = ' '
        unit = ' '
        val = 0.0
        inpu()
    elif ch=='N':
        exit()
    else:
        print("Invalid Entry")
        again()
inpu()


# In[ ]:




