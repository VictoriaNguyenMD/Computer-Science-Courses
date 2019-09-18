"""
Very nice! For another challenge, how about writing a function to find the first element in a list that does not repeat?

So, for example, in the list [1, 2, 3, 3, 1, 4], the output would be 2.
"""

def inner_loop(list_test, outer_val, outer_index): #compare outer num to the numbers inside it
  boolean_list = []
  inner_index = 0

  for i in list_test: #Converts to a boolean list
    boolean_list.append(i == outer_val and inner_index != outer_index)
    inner_index += 1

  if True not in boolean_list: #if the outer loop value is not in the list
    return True


def outer_loop(list_test, outer_index): #retrieve the outer num
  while(outer_index < len(list_test)):
    outer_val = list_test[outer_index]

    if(inner_loop(list_test, outer_val, outer_index)): #if the outer num is not repeated, returns this
      return print("This is the answer: " + str(outer_val))
    else:
      inner_loop(list_test, outer_val, outer_index)
    outer_index += 1

def user_input():
  list_user_num = []
  user_num = input("Write a string of numbers: " )
  i = 0
  while(i < len(user_num)):
    list_user_num.append(int(user_num[i]))
    i += 1
  return list_user_num


#The main function we're running
outer_loop(user_input(), 0)
