#!/usr/bin/python
# dice10k.py
# By: Kyle Roux (aka:aMigOd666)
# a fun game of 10000 using unicode 
# pics of dice. fun
########################################

########################################
# INITALIZATION 
########################################

# here are the imports, needed for randomness
# as well as the unicode (python dosent like it)
# so we borrow from perl
import commands
import random

# make sure we play at least one game
PLAY = 'y'
FullTotal = 0
#global SCORE1 
#SCORE1 = 0
#global SCORE
#SCORE = 0
#global SCORE2
#SCORE2 = 0
global theScore
#theScore = 0

#######################################################
# function defs # 				      #
#################                                     #
#	chk_face 		                      #
# 						      #
# check the face of a die so you know which it was    #
#######################################################
def chk_face(dce):
    if dce == a1:
      dice_face = 1
    elif dce == a2:
      dice_face = 2
    elif dce == a3:
      dice_face = 3
    elif dce == a4:
      dice_face = 4
    elif dce == a5:
      dice_face = 5
    else:
      dice_face = 6
    return dice_face
    
###########################################
#    triple_chk 			  #
#    					  #
#  	check if any face is 3 or higher  #
###########################################    
def triple_chk(dnum, face):
    score = 0
    if dnum >= 3:
      if dnum == 3:
        score = face * 100
      elif dnum == 4:
        score = (face * 100) * 2 
      elif dnum == 5:
        score = ((face * 100) * 2) * 2
      else:
        score = (((face * 100) * 2) * 2) * 2
    return score

##########################################
#                                        #
#  noThreeOrMore() 			 #
#        make sure there are a bunch of  #
#        ones and fives before assigning #
#        scores 			 #
##########################################
def noThreeOrMore(dce):
  global SCORE1 
  global SCORE5
  if count_list[0] <= 2:
    if dce == a1:
      SCORE1 = 100
    else:
      SCORE1 = 0

  if count_list[4] <=2:
    if dce == a5:
      SCORE5 = 50
    else:
      SCORE5 = 0
  theScore = SCORE1 + SCORE5
  return theScore

# initial random seed (do it again)
random.seed()

# here we assign the pics to variables via external perl scripts
a1 = commands.getoutput('d1')
a2 = commands.getoutput('d2')
a3 = commands.getoutput('d3')
a4 = commands.getoutput('d4')
a5 = commands.getoutput('d5')
a6 = commands.getoutput('d6')

# now we assign list 1-6 all six faces of a die.
# this effectivly gives us six dice.
list1 = [a1,a2,a3,a4,a5,a6]
list2 = [a1,a2,a3,a4,a5,a6]
list3 = [a1,a2,a3,a4,a5,a6]
list4 = [a1,a2,a3,a4,a5,a6]
list5 = [a1,a2,a3,a4,a5,a6]
list6 = [a1,a2,a3,a4,a5,a6]

while PLAY == 'y':
  total = 0
  myTotal = 0
  SCORE1 = 0
  score = 0
  SCORE5 = 0
  SCORE = 0
  theScore = 0
  S1 = 0

  d1, d2, d3, d4, d5, d6 = 0, 0, 0, 0, 0, 0
  D1, D2, D3, D4, D5, D6 = 0, 0, 0, 0, 0, 0
	
  # now we roll the dice
  dce1 = random.choice(list1)
  dce2 = random.choice(list2)
  dce3 = random.choice(list3)
  dce4 = random.choice(list4)
  dce5 = random.choice(list5)
  dce6 = random.choice(list6)
  
  # this is our roll
  dice_list = [dce1, dce2, dce3, dce4, dce5, dce6]
  
  # now lets start checking
  
  #first lets check how many of each 'die' we have
  # a1-a6 represents dice face 1-6 
  # so here we count a's and assign them to d's
  for y in dice_list:
    if y == a1:
      d1 +=1
    elif y == a2:
      d2 +=1
    elif y == a3:
      d3 +=1
    elif y == a4:
      d4 +=1
    elif y == a5:
      d5 +=1
    else:
      d6 +=1
  
  # now d1-d6 hold how many of each die were rolled
  count_list = [d1, d2, d3, d4, d5, d6]
  
  # now check for a strait : 1,2,3,4,5,6
  if total == 0:
    if count_list[0] == 1:
      if count_list[1] == 1:
        if count_list[2] == 1:
          if count_list[3] == 1:
            if count_list[4] == 1:
              if count_list[5] == 1:
                myTotal = 1000
    
  # now lets check how many ones (it scores diffrently)
  if myTotal == 0:
    if count_list[0] >= 3:
      if count_list[0] == 3:
        S1 = 1000
      elif count_list[0] == 4:
        S1 = 2000
      elif count_list[0] == 5:
        S1 = 4000
      else:
        S1 = 8000

  face1 = chk_face(dice_list[0])
  face2 = chk_face(dice_list[1])
  face3 = chk_face(dice_list[2])    
  face4 = chk_face(dice_list[3])      
  face5 = chk_face(dice_list[4])    
  face6 = chk_face(dice_list[5])
  
  #print("Face1 is ", face1)
  #print("face2 is ", face2)
  #print("face3 is ", face3)
  #print("face4 is ", face4)
  #print("face5 is ", face5)
  #print("face6 is ", face6)
  print count_list
  
  if myTotal == 0:
    F2 = triple_chk(count_list[1], face2)
    F3 = triple_chk(count_list[2], face3)
    F4 = triple_chk(count_list[3], face4)
    F5 = triple_chk(count_list[4], face5)
    F6 = triple_chk(count_list[5], face6)
   
    DG2 = triple_chk(d2, face2)
    DG3 = triple_chk(d3, face3)
    DG4 = triple_chk(d4, face4)
    DG5 = triple_chk(d5, face5)
    DG6 = triple_chk(d6, face6)
	
    GD2 = triple_chk(face2, d2)
    GD3 = triple_chk(face3, d3)
    GD4 = triple_chk(face4, d4)
    GD5 = triple_chk(face5, d5)
    GD6 = triple_chk(face6, d6)
	
  ''' if D1 == 0 and D5 == 0:
        if dce1 == a1: 
          D1 = 100
        elif dce1 == a5:
          D1 = 50
        else: 
          D1 = 0

      if D2 == 0:
        if dce2 == a1: 
          D2 = 100
        elif dce2 == a5:
          D2 = 50
        else: 
          D2 = 0


      if D3 == 0:
        if dce3 == a1: 
          D3 = 100
        elif dce3 == a5:
          D3 = 50
        else: 
          D3 = 0

      if D4 == 0:
        if dce4 == a1: 
          D4 = 100
        elif dce4 == a5:
          D4 = 50
        else: 
          D4 = 0

      if D5 == 0:
        if dce5 == a1: 
          D5 = 100
        elif dce5 == a5:
          D5 = 50
        else: 
          D5 = 0
  
      if D6 == 0:
        if dce6 == a1: 
          D6 = 100
        elif dce6 == a5:
          D6 = 50
        else: 
          D6 = 0 '''
  D1 = noThreeOrMore(dce1)
  D2 = noThreeOrMore(dce2)
  D3 = noThreeOrMore(dce3) 	
  D4 = noThreeOrMore(dce4) 	  
  D5 = noThreeOrMore(dce5) 	   
  D6 = noThreeOrMore(dce6) 	  

  myTotal = S1 + D1 + D2 + D3 + D4 + D5 + D6 + F2 + F3 + F4 + F5 + F6
  FullTotal = FullTotal + myTotal
  DG1 = 0
  GD1 = 0
  
  print dce1, " ", dce2, " ", dce3, " ", dce4, " ", dce5, " ", dce6
  print D1, " ", D2, " ", D3, " ", D4, " ", D5, " ", D6
  #print DG1, " ", DG2, " ", DG3, " ", DG4, " ", DG5, " ", DG6
  #print GD1, " ", GD2, " ", GD3, " ", GD4, " ", GD5, " ", GD6
  
  # print results
  print 'this hand you got', myTotal
  print 'your total is', FullTotal

  # ask player to play again
  print 'Would you like to play again (y or n)?'
  
  PLAY = raw_input()


print 'Thanks for playing, have a great day!!'
  
  
  
  
