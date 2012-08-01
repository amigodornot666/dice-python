#!/usr/bin/python
# a fun game of 10000 using unicode 
# hope this works
# pics of dice

# heres the imports, needed for randomness
# as well as the unicode (python dosent like it)
import commands
import random

# here we assign the pics to variables
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

# we need to seed so we actually get a random number
random.seed()

PLAY = 'y'


FullTotal = 0

while PLAY == 'y':
  TOTAL = 0
  d1, d2, d3, d4, d5, d6 = 0, 0, 0, 0, 0, 0
  # now we roll the dice
  dce1 = random.choice(list1)
  dce2 = random.choice(list2)
  dce3 = random.choice(list3)
  dce4 = random.choice(list4)
  dce5 = random.choice(list5)
  dce6 = random.choice(list6)

  dice_list = [dce1,dce2,dce3,dce4,dce5,dce6]

  D1 = 0
  D2 = 0
  D3 = 0
  D4 = 0
  D5 = 0
  D6 = 0

  # test for 3 or more nums
  #CHK1 = dice_list.count(a1)
  #CHK2 = dice_list.count(a2)
  #CHK3 = dice_list.count(a3)
  #CHK4 = dice_list.count(a4)
  #CHK5 = dice_list.count(a5)
  #CHK6 = dice_list.count(a6)
  
   
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
  
  count_list = [d1, d2, d3, d4, d5, d6]
  MY_TOTAL = 0
  print count_list

  if TOTAL == 0:
    if count_list[0] == 1:
      if count_list[1] == 1:
        if count_list[2] == 1:
          if count_list[3] == 1:
            if count_list[4] == 1:
              if count_list[5] == 1:
                MY_TOTAL = 1000
  TOTAL = MY_TOTAL


  if TOTAL == 0:
    if count_list[0] >= 3:
      if count_list[0] == 3:
        D1 = 1000
      elif count_list[0] == 4:
        D1 = 2000
      elif count_list[0] == 5:
        D1 = 4000
      else:
        D1 = 8000

  print D1
  
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

  face1 = chk_face(dice_list[0])
  face2 = chk_face(dice_list[1])
  face3 = chk_face(dice_list[2])    
  face4 = chk_face(dice_list[3])      
  face5 = chk_face(dice_list[4])    
  face6 = chk_face(dice_list[5])    
  
  # DEBUG
  #print 'faces', face_list

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
  
  # check for 3 or more of a kind
  if TOTAL == 0:
    #if count_list[1] >= 3:
    D2 = triple_chk(count_list[1], face2)
    #if count_list[2] >= 3:
    D3 = triple_chk(count_list[2], face3) 
    #if count_list[3] >= 3:
    D4 = triple_chk(count_list[3], face4)
    #if count_list[4] >= 3:
    D5 = triple_chk(count_list[4], face5)
    #if count_list[5] >= 3:
    D6 = triple_chk(count_list[5], face6)

  #DEBUG
  print 'SCORE DEBUG ', D1, " ", D2, " ", D3, " ", D4, " ", D5, " ", D6


  # assign the scores
  if TOTAL == 0:
    if D1 != 0:
      D1 = D1    
    elif dce1 == a1: 
      D1 = 100
    elif dce1 == a5:
      D1 = 50
    else: 
      D1 = 0

    if D2 != 0:
      D2 = D2
    elif dce2 == a1: 
      D2 = 100
    elif dce2 == a5:
      D2 = 50
    else: 
      D2 = 0


    if D3 != 0:
      D3 = D3
    elif dce3 == a1: 
      D3 = 100
    elif dce3 == a5:
      D3 = 50
    else: 
      D3 = 0

    if D4 != 0:
      D4 = D4
    elif dce4 == a1: 
      D4 = 100
    elif dce4 == a5:
      D4 = 50
    else: 
      D4 = 0

    if D5 != 0:
      D5 = D5
    elif dce5 == a1: 
      D5 = 100
    elif dce5 == a5:
      D5 = 50
    else: 
      D5 = 0
  
    if D6 != 0:
      D6 = D6
    elif dce6 == a1: 
      D6 = 100
    elif dce6 == a5:
      D6 = 50
    else: 
      D6 = 0



  #Blank = commands.getoutput("clear")

  #print Blank


  #print xtra
  print dce1, " ", dce2, " ", dce3, " ", dce4, " ", dce5, " ", dce6
  print D1, " ", D2, " ", D3, " ", D4, " ", D5, " ", D6
  
  TOTAL = D1 + D2 + D3 + D4 + D5 + D6
  FullTotal = FullTotal + TOTAL
	
  # print checks
  #print CHK1 
  #print CHK2
  #print CHK3
  #print CHK4
  #print CHK5
  #print CHK6
  
  # print results
  print 'this hand you got', TOTAL
  print 'your total is', FullTotal

  # ask player to play again
  print 'Would you like to play again (y or n)?'
  
  PLAY = raw_input()


print 'Thanks for playing, have a great day!!'
