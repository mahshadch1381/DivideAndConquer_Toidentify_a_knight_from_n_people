import random
import sys
import math
from human import human

c = []
#b = []
def only_one():
    print("number_of_knights: 1")
    print("number_of_liars: 0")
    print("all humans: [True]")
    print(0)
    sys.exit()
    
def only_two():
    print("number_of_knights: 2")
    print("number_of_liars: 0")
    print("all humans: [True, True]")
    print(0)
    print(1)
    sys.exit()
def liar_answer():
    quilifiers = [True,False]
    s = random.randint(0, 1)
    return quilifiers[s]


def difinig_humans():
    humans = []
    number_of_humans = int(input("Enter the number of humans: "))
    if(number_of_humans <= 0):
        print("wrong input!")
        sys.exit()
    elif(number_of_humans == 1):
        only_one()
    elif(number_of_humans == 2):
        only_two()
    
    half = number_of_humans//2 + 1
    number_of_knights = random.randint(half, number_of_humans)
    number_of_liars = number_of_humans - number_of_knights
    print("number_of_knights:",number_of_knights)
    print("number_of_liars:",number_of_liars)
    n_k = 0
    n_o = 0
    for i in range( number_of_humans):
        
        if(number_of_liars == 0):
            break
        tmp = liar_answer()
        if(tmp):
            n_k += 1
            humans.append(human(True))
            if(n_k >= number_of_knights):
                break
        else:
            n_o += 1
            humans.append(human(False))
            if(n_o >= number_of_liars):
                break
    while(n_k < number_of_knights):
        humans.append(human(True))
        n_k += 1
    while(n_o < number_of_liars):
        humans.append(human(False))
        n_o += 1
        
    return humans



def convert_to_power_2(arr):
    a = math.log(len(arr), 2)
    #print(a)
    if(a == int(a)):
        return 
    else:
        a = 2 ** (int(a)+1)
        a = a - len(arr)
        arr.extend(["-"]*int(a))
    
def find_knight(arr):
    
    if(len(arr) == 1 or len(arr) == 2):
        return arr[0]
    elif(len(arr) == 3):
        a0 = 0
        a1 = 0
        a2 = 0
        if(arr[0].is_knight):
            if(arr[1].is_knight):
                a1+=1
            if(arr[2].is_knight):
                a2+=1
        else:
            a1 += random.randint(0, 1)
            a2 += random.randint(0, 1)
            
        if(arr[1].is_knight):
            if(arr[0].is_knight):
                a0+=1
            if(arr[2].is_knight):
                a2+=1
        else:
            a0 += random.randint(0, 1)
            a2 += random.randint(0, 1)
                
        if(arr[2].is_knight):
            if(arr[0].is_knight):
                a0+=1
            if(arr[1].is_knight):
                a1+=1
        else:
             a0 += random.randint(0, 1)
             a1 += random.randint(0, 1)
        #print(a0,a1,a2)
        if(a0 >= 1):
            return arr[0]
        if(a1 >= 1):
            return arr[1]
        if(a2 >= 1):
            return arr[2]
    
def find_one_knight(arr, l, r):
   
    if l + 2 < r:
 
        m = l+(r-l)//2
        find_one_knight(arr, l, m)
        find_one_knight(arr, m+1, r)
        find_knight_from_two(arr, l, m, r) 

def ask_each_other(arr,b):
    
    if(len(b) == 0):
        return
    if(len(b) == 1):
            return
        
    if b[0] == b[1] == "-":
        return 
    elif b[0] == "-":
        c.append(b[1])
    elif b[1] == "-":
        c.append(b[0])
    else:
        if(b[0].is_knight):
            a1 = b[1].is_knight
        else:
            a1 = liar_answer()
        if(b[1].is_knight):
            a2 = b[0].is_knight
        else:
            a2 = liar_answer()
        if(a1 and a2):
            c.append(b[0])
            
def find_knight_from_two(arr, l, m, r):
    if(m-l == 2):
         ask_each_other(arr,arr[l:m])
         #b.append(arr[l:m])
    elif(m-l == 1):
         ask_each_other(arr,arr[l-1:m])
         #b.append(arr[l-1:m])
    if(r-m == 2):
         ask_each_other(arr,arr[m:r])
         #b.append(arr[m:r])
    elif(r-m == 1):
         ask_each_other(arr,arr[m-1:r])
         #b.append(arr[m-1:r])
    if(r-l == 2):
         ask_each_other(arr,arr[l:r])
         #b.append(arr[l:r])
    elif(r-l == 1):
         ask_each_other(arr,arr[l-1:r]) 
         #b.append(arr[l-1:r])

def find_other_knights(humans2):
    humans2.remove(a)
    print()
    print("selected from algorithm :",humans.index(a))
    print("Others:")
    k=1
    for i in humans2:
        if(i == "-"):
            break
        
        if(i.is_knight):
            k+=1
            print(" ",humans.index(i))

    
humans = difinig_humans()
print("all humans:",humans)


humans2 = humans.copy()    
convert_to_power_2(humans2)


if(len(humans2) == 3):
    a = find_knight(humans2)
else:    
    while 1:
        
        find_one_knight(humans2,0,len(humans2))
        if(len(c) <= 3):
            break
    
        if(len(c)!=0):
            convert_to_power_2(c)
        humans2 = c.copy()
        c = []
    
a = find_knight(c)

humans2 = humans.copy()

find_other_knights(humans2)

