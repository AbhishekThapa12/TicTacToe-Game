# Import the Libraries :

import os
import math
import numpy as np

# Initialize the Variables to be used :

# arr - 3 x 3 Matrix -> Used for marking 'o' and 'x'

arr = [['','',''],
     ['','',''],
     ['','','']]

# Index Positions :

pos = [[(0,0),(0,1),(0,2)],
       [(1,0),(1,1),(1,2)],
       [(2,0),(2,1),(2,2)]]

#  now - keeps track of whose turn it is now i.e Player 1 or 2

now = 0

# won -> to know which player won
# 0 = No one, 1 = Player1 won, 2 = Player2 won

won = 0

# 'first' value tells us if it's the beginning of the game / 1st move of the game : 

first = 0

#  Functions to check if someone has completed a line :

# Horizontal Check Function:

def check_horizontal():
  for i in arr:
    if(i[0]==i[1]) and (i[1] == i[2]) and (i[1] != ''):
      return i[0]
  return 0;
  
# Vertical Check Function:

def check_vertical():
  transpose_arr = np.transpose(arr)
  for i in transpose_arr:
    if(i[0]==i[1]) and (i[1] == i[2]) and (i[1] != ''):
      return i[0]
  return 0;
  
# Diagonal Check Function :

def check_diagonal():
  if(arr[0][0] == arr[1][1]) and (arr[1][1] == arr[2][2]) and (arr[1][1] != ''):
      return arr[0][0]
  elif(arr[0][2] == arr[1][1]) and (arr[1][1] == arr[2][0]) and (arr[1][1] != ''):
      return arr[0][2]
  else:
      return 0;
	  
# Main Function :

print('\n\n Tic Tac Toe Game : ')
print('\n\n "o" - Player1 and "x" - Player2')

#  Refresh won, arr and first values for a new game:

won = 0

arr = [['','',''],
     ['','',''],
     ['','','']]

first = 0

while(won == 0):
  # In the Beginning of Game, Ask for who want's to go first:
  if(first == 0):
    print("\n\n Who want's to go first : Player1 -> 1 or Player2 -> 2")
    now = int(input())
    player_no = now 

  # If it's not the beginning, switch the player_no 's value so that both player play's at alternate turns
  if(player_no == 1) and (first != 0):
    player_no = 2
  elif(player_no == 2) and (first != 0):
    player_no = 1
  print("\n\n Player No. {}'s Chance : ".format(player_no))

  # Ask for Player's move i.e Row & Column number
  x = int(input('\n Your Move -> Row Number : '))
  y = int(input('\n Your Move -> Column Number : '))
  if(player_no == 1):
      arr[x][y] = 'o'
  else:
      arr[x][y] = 'x'
  print('\n\n')

  # Print the array after every move:
  for a in arr: 
    print(a)

  # Check if someone won the game : Horizontal, Vertical, Diagonal
  res1 = check_horizontal()
  res2 = check_vertical()
  res3 = check_diagonal()
  if(res1 != 0 or res2 != 0 or res3 != 0):
      won = player_no
      print('\n Player {0} won '.format(player_no))
  
  # If no one wins, The Game continues :
  if(won == 0):
      print('\n\n Game Continues :')

  # first = 1 after the first move
  first = 1

        
