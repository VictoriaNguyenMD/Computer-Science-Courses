""""Given a sorted array, count the occurences of a given number which may or may not be present in the array in log n time. Prior to this problem, GRI Gabe asked me if I knew recursion"""

class Answer():
  def __init__(self, array):
    self.array = array

  def start_loc(self, low, high):
    mid = int((low + high)/2)

    #The condition for the recursion to end
    if array[mid] == val: #Finds desired value
      if mid == 0: #Check if index is at 0 index, need to do this bc you cant do mid - 1 else it'll become array[-1]
        return mid
      elif array[mid-1] < val: #If not 0 index, then make sure index-1 is less
        return mid
    elif (high - low == 1): #If value is not found
      return 0

    if val <= array[mid]:#Desired val is less than the middle
      high = mid
      return self.start_loc(low, high)
    else: #Desired val is greater than the middle
      low = mid
      return self.start_loc(low, high)


  def end_loc(self, low, high):
    mid = int((low + high)/2)
    if array[mid] == val: #Finds desired value
      if mid == (len(array) - 1): #Check if the last element in the list, need to do this bc you cant do mid + 1 else it'll become out of bound
        return mid
      elif array[mid+1] > val: #If not last index, then make sure index+1 is greater
        return mid
    elif (high - low == 1): #If value is not found
      return 0

    if val >= array[mid]:#Desired val is greater than middle
      low = mid
      return self.end_loc(low, high)
    else: #Desired val is less than middle
      high = mid
      return self.end_loc(low, high)

  def count(self):
    start = self.start_loc(0, len(self.array))
    end = self.end_loc(0, len(self.array))

    if (end-start) != 0:
      return ((end-start)) + 1 # +1 because it is inclusive
    else: #Value is not in the list
      return 0 


#Asking what val
val = int(input("Write a val: "))

#Instance of Answer
array = [0,1,1,1,1,1,1,2,3,3]
# array = [-10, -2, -2, 3, 4, 4, 5]
answer = Answer(array)

print(answer.count())

#Output
print("\nThis program will count the number of '{}'s in this array.".format(val))
print("Array: " + str(list(val for val in array)))
print("\nThe length of this array: {}".format(len(array)))
print("The desired value: {}".format(val))
print("'{}' Count: ".format(val) + str(answer.count()))

