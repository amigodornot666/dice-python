#!/usr/bin/python
import commands
import random

a1 = commands.getoutput('d1')
a2 = commands.getoutput('d2')
a3 = commands.getoutput('d3')
a4 = commands.getoutput('d4')
a5 = commands.getoutput('d5')
a6 = commands.getoutput('d6')

list1 = [a1,a2,a3,a4,a5,a6]
list2 = [a1,a2,a3,a4,a5,a6]
list3 = [a1,a2,a3,a4,a5,a6]
list4 = [a1,a2,a3,a4,a5,a6]
list5 = [a1,a2,a3,a4,a5,a6]
list6 = [a1,a2,a3,a4,a5,a6]

random.seed()

dce1 = random.choice(list1)
dce2 = random.choice(list2)
dce3 = random.choice(list3)
dce4 = random.choice(list4)
dce5 = random.choice(list5)
dce6 = random.choice(list6)

print dce1, " ", dce2, " ", dce3, " ", dce4, " ", dce5, " ", dce6

if dce1 == a1: 
  D1 = 100
elif dce1 == a5:
  D1 = 50
else: 
  D1 = 0

if dce2 == a1: 
  D2 = 100
elif dce1 == a5:
  D2 = 50
else: 
  D2 = 0

if dce3 == a1: 
  D3 = 100
elif dce1 == a5:
  D3 = 50
else: 
  D3 = 0

if dce4 == a1: 
  D4 = 100
elif dce1 == a5:
  D4 = 50
else: 
  D4 = 0

if dce5 == a1: 
  D5 = 100
elif dce1 == a5:
  D5 = 50
else: 
  D5 = 0

if dce6 == a1: 
  D6 = 100
elif dce1 == a5:
  D6 = 50
else: 
  D6 = 0

print D1, " ", D2, " ", D3, " ", D4, " ", D5, " ", D6
