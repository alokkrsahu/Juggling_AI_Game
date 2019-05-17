# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:38:36 2019

@author: alokk
"""
import random
from goto import with_goto
class Node(object):
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node
        self.prev = None #
#-----------TOTAL VOLUME--------------#
vol1 = 5
vol2 = 3
vol3 = 8        

#-----------FINAL GOAL VOLUME---------#
goal1 = 4
goal2 = 0
goal3 = 4

#-----------INITIAL VOLUME------------#        
jug1 = 5 #initial volume of jug1
jug2 = 3 #initial volume of jug2
jug3 = 0 #initial volume of jug3


V = Node()
X = Node()
W = Node()

V.prev = jug1
V.data = jug2
V.next = jug3


flag = 1
while (V.prev <= vol1 or V.data <= vol2 or V.next <=vol3):

    if (V.prev == 4 and V.next == 4):
        print("Goal State Reached")
        break
#EMPTY JUG 2 INTO JUG 1 OR JUG 3
#-------------------V NODE JUGGLING------------------#    
    r = random.randint(0,1)

    if flag == 1:
        while (V.data > 0 and V.prev < vol1 and r==0): #EXECUTE TILL JUG 2 IS EMPTIED ON JUG 1
                if (V.prev < vol1):
                    V.data = V.data - 1
                    V.prev = V.prev + 1
                if V.data > 0 :
                    flag = 1
                else :  
                    flag = 2
                   # print("Loop1")
        
    if flag == 1:
        while (V.data > 0 and V.next < vol3 and r==1): #EXECUTE TILL JUG 2 IS EMPTIED ON JUG 3 
                if (V.next < vol3):
                    V.data = V.data - 1
                    V.next = V.next + 1
                if V.data > 0:
                    flag = 1
                    r = 0
                else :
                    flag = 2
                    #print("Loop2")

         

                    
    print("I ","1st-------",V.prev,"2nd-------",V.data,"3rd-------",V.next)        



    
    W.prev = V.data             # JUG2 IS IN POSITION 1        
    W.data = V.next             # JUG3 IS IN POSITION 2
    W.next = V.prev             # JUG1 IS IN POSITION 3
#EMPTY JUG 3 INTO JUG 2 OR JUG 1    
#-----------------W NODE JUGGLING-------------------#

    if flag == 2:
        r = random.randint(0,1)        
        while (W.data > 0 and W.prev < vol2 and r == 0): #
                if (W.prev < vol2):
                    W.data = W.data - 1
                    W.prev = W.prev + 1
                if W.data > 0:
                    flag = 2
                else :
                    flag = 3
                  #  print("Loop3")        
        
    if flag == 2:                
        while (W.data > 0 and W.next < vol1 and r==1):
                if (W.next < vol3):
                    W.data = W.data - 1
                    W.next = W.next + 1
                if W.data > 0:
                    flag = 2
                    r = 0
                else :
                    flag = 3
                   # print("Loop4")        

                    
    print("II ","1st-------",W.next,"2nd-------",W.prev,"3rd-------",W.data)                            

#-----------------X NODE JUGGLING-------------------#        

    
    X.prev = W.data             #JUG3 IS IN POSITION 1        
    X.data = W.next             #JUG1 IS IN POSITION 2
    X.next = W.prev             #JUG2 IS IN POSITION 3

# EMPTY JUG 1 INTO JUG 3 OR JUG 2

    if flag == 3:
        r = random.randint(0,1)
        while (X.data > 0 and X.prev < vol3 and r == 0):
                if (X.prev < vol3):
                    X.data = X.data - 1
                    X.prev = X.prev + 1
                if X.data > 0:
                    flag = 3
                else :
                    flag = 1

                   # print("Loop 5")
        
    if flag == 3 and r == 1:                
        while (X.data > 0 and X.next < vol2 and r == 1):
                if (X.next < vol2):
                    X.data = X.data - 1
                    X.next = X.next + 1  
                if X.data > 0:
                    flag = 3
                    r = 0
                else:
                    flag = 1
                    #print("Loop6")            

    print("III ","1st-------",X.data,"2nd-------",X.next,"3rd-------",X.prev)                            
    V.prev = X.data             #JUG 1
    V.data = X.next             #JUG 2
    V.next = X.prev             #JUG 3

       
                    

    

        
        
        
        
        
        
        
#    def start_juggling (c1,c2,c3):
#
#        while (c2 == 0):
#        
#                if (c1 <= C1):
#                    c2 = c2 - 1
#                    c1 = c1 + 1
#                    
#                elif (c3 <= C3):
#                    c2 = c2 - 1
#                    c3 = c3 + 1