3#Tic-Tac-Toe Game. There should be a total of five functions: move_x, move_o, print_board, check_winner, and check_full. The check_winner should return "x" or "o" or None. The goal is to have a functional game that allows for other players to players

from players import Players

class TicTacToe:
  
  def __init__(self, player_1, player_2):
    self.array_locations = [[0,1,2],[0,1,2],[0,1,2]]
    self.player_1 = player_1
    self.player_2 = player_2
    self.player_turn = 1
    self.max_num = 9

  def change_array(self): 
    if self.player_turn % 2 == 1:
      user_val = self.player_1.move_x()
    else:
      user_val = self.player_2.move_o()

    a = user_val[0]
    b = user_val[1]
    
    outer_i = 0

    for outer in self.array_locations:
      inner_i = 0
      for v in outer:
        if(outer_i == a and inner_i == b):
          if(self.array_locations[outer_i][inner_i] == "X" or self.array_locations[outer_i][inner_i] == "O"):
            print("This spot is already taken. Please input a new 'row' and 'col' value.")
            return board.change_array()
          self.array_locations[outer_i][inner_i] = user_val[2]
        inner_i += 1
      outer_i += 1
  
  def print_board(self):
    outer_i = 0
    bottom_line = 0

    print("\nTic-Tac-Toe")

    for outer in self.array_locations: 
      for inner in outer: 
        if inner == 'X' or inner == 'O': 
          print(str(inner), end = " | ")
        else: 
          print(" ", end = " | ")
      if bottom_line < 2: 
        print("\n" + "___________")
        bottom_line += 1
      outer_i += 1
    
  def check_winner(self): #outer index, inner index, cross
    win1_p1 = ["X","X","X"] #Horizontal. Player 1
    win1_p2 = ["O","O","O"] #Horizontal: Player 2

    for outer in self.array_locations: #Horizontal
      if outer == win1_p1:
        print("Player 1 is a winner.")
        return True
      elif outer == win1_p2:
        print("Player 2 is a winner.")

    index_v = 0
    
    while index_v < 3: #Vertical
      temp_list_v = []
      for outer in self.array_locations:
        temp_list_v.append(outer[index_v]) 
        if temp_list_v == win1_p1:
          print("Player 1 is the winner")
          return True
        elif temp_list_v == win1_p2:
          print("Player 2 is the winner")
          return True
      index_v += 1

      index_LRDiag = 0
      index_RLDiag = 2
      temp_list_LRDiag = []
      temp_list_RLDiag = []

    for outer in self.array_locations:
      temp_list_LRDiag.append(outer[index_LRDiag])
      temp_list_RLDiag.append(outer[index_RLDiag])
      
      if temp_list_LRDiag == win1_p1 or temp_list_RLDiag == win1_p1:
          print("Player 1 is the winner")
          return True
      elif temp_list_LRDiag == win1_p2 or temp_list_RLDiag == win1_p2:
          print("Player 2 is the winner")
          return True
      index_LRDiag += 1
      index_RLDiag -= 1

  def check_full(self):
    if self.player_turn == self.max_num:
      print("\n\nThe board is full. There are no winners.")
      return True
    self.player_turn += 1
    return False

#Playing the Game
player_1 = Players()
player_2 = Players()

print("Player 1: " + player_1.name + ". You will use 'X'")
print("Player 2: " + player_2.name + ". You will use 'O'")

board = TicTacToe(player_1, player_2)

array_locations = [[0,1,2],[0,1,2],[0,1,2]]
outer_i = 0
bottom_line = 0

print("\n Row/Column Vals")
for outer in array_locations:
  for inner_i in outer:
    print(str(outer_i) + "," + str(inner_i), end = " | ")
  if bottom_line < 2:
    print("\n" + "_________________")
    bottom_line += 1
  outer_i += 1

while(not board.check_winner()):
  board.change_array()
  board.print_board()

  board.check_full()
