#!/usr/bin/python
print('Welcome to a fun game of dice!')
print('We call this game 10,000.')
print('Whats your name? You\'ll be player 1')
NAME = raw_input()
print "Nice to meet you", NAME, "you read to play?"
print("first i need to know if your familiar with the rules? (y or n)")
CHOICE = raw_input()

if CHOICE == 'y':
  print NAME, "knows the game. nice."
else:
  print NAME, "dont know shit."

#!/usr/bin/python
# a fun game of 10000 using unicode 
# pics of dice

# heres the imports, needed for randomness
# as well as the unicode (python dosent like it)
import commands
import random
import collections 

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
  # now we roll the dice
  dce1 = random.choice(list1)
  dce2 = random.choice(list2)
  dce3 = random.choice(list3)
  dce4 = random.choice(list4)
  dce5 = random.choice(list5)
  dce6 = random.choice(list6)

  dice_list = [dce1,dce2,dce3,dce4,dce5,dce6]
  
  xtraPointCount = collections.Counter(dice_list)
  
  print xtraPointCount[dce1]
  print xtraPointCount[dce2]
  print xtraPointCount[dce3]
  print xtraPointCount[dce4]
  print xtraPointCount[dce5]
  print xtraPointCount[dce6]
  
  #occurances = collections.defaultdict(lambda:0)

  #for n in dice_list: 
	#occurances[n] += 1
	#if occurances[n] >= 3:
	  #print occurances[n]


  # assign the scores
  if dce1 == a1: 
    D1 = 100
  elif dce1 == a5:
    D1 = 50
  else: 
    D1 = 0

  if dce2 == a1: 
    D2 = 100
  elif dce2 == a5:
    D2 = 50
  else: 
    D2 = 0

  if dce3 == a1: 
    D3 = 100
  elif dce3 == a5:
    D3 = 50
  else: 
    D3 = 0

  if dce4 == a1: 
    D4 = 100
  elif dce4 == a5:
    D4 = 50
  else: 
    D4 = 0

  if dce5 == a1: 
    D5 = 100
  elif dce5 == a5:
    D5 = 50
  else: 
    D5 = 0

  if dce6 == a1: 
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
  print 'this hand you got', TOTAL
  print 'your total is', FullTotal
  print 'Would you like to play again (y or n)?'
  
  PLAY = raw_input()


print 'Thanks for playing', NAME, '. Woah you finished with', FullTotal,'points. Have a great day!!'
