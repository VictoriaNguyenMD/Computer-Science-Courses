class Players:
  def __init__(self):
    self.name = input("Write a name: ")
 
  def move_x(self):
    x = -1
    y = -1

    while((x > 2 or x < 0) or  (y > 2 or y < 0)):
      input_val = (input("\n\nPlayer 1: which 'row,column' position do you want to move to?: "))
      try:
        x = int(input_val.split(",")[0])
        y = int(input_val.split(",")[1])
      except:
        print("Input must be in the form row,column")
    
    return x,y,"X"
  
  def move_o(self):
    
    x = -1
    y = -1

    while ((x < 0 or  x > 2) or (y > 2 or y < 0)):
      val = input("\n\nPlayer2: which 'row,column' position do you want to move to?: ")
      try:
        x = int(val.split(",")[0])
        y = int(val.split(",")[1])
      except:
        print("Input must be in the form row,column")
        
    return x,y,"O"


