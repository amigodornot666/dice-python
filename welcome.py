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

