class List():
    def __init__(self, max_in):
        self.max_in = max_in
        self.array = [None]*max_in
        self.index_end = 0
    
    def append(self, val):
        if self.index_end == self.max_in:
            print("The array is full!")
            return None
        self.array[self.index_end] = val
        self.index_end += 1
    
    def extend(self, list_in): #A list is the parameter rather than the value
        for val in list_in:
            self.append(val)
        # print(self.array)
            
    def insert(self, index, val):
        temp = self.max_in - 1
        for i in range(temp - 1):
            if i == index:
                while temp != i:
                    self.array[temp] = self.array[temp-1]
                    temp -= 1
        self.array[index] = val
                
    def remove(self, val):
        for i in range(self.max_in):
            if val == self.array[i] and i < self.max_in - 1:
                temp = i 
                while temp < self.max_in - 1:
                   print(self.array[temp])
                   print(str(self.array[temp + 1]))
                   print(self.array)
                   self.array[temp] = self.array[temp + 1]
                   temp += 1
                   print(self.array)
                
                self.array[self.max_in-1] = None
                break
               
            
    def pop(self, index = None):
        if index == None:
            for i in range (self.max_in):
                if i == self.max_in - 1:
                    self.array[i] = None
                elif self.array[i + 1] == None:
                    self.array[i] = None
            
        for i in range(self.max_in):
            if index == i:
                temp = self.array[i]
                if i == self.max_in:
                    self.array[i] = None
                else:
                    curr = i
                    while curr <= self.max_in - 2:
                        self.array[curr] = self.array[curr + 1]
                        self.array[curr + 1] = None
                        curr += 1
                    return temp
            
    def clear(self): #Remove everything
        for i in range(self.max_in):
            self.index_end = 0
            self.array[i] = None
    
    def index(self, val):
        for i in range(self.max_in):
            if self.array[i] == val:
                return i
    
    def count(self, val):
        temp = 0
        for i in range(self.max_in):
            if self.array[i] == val:
                temp += 1
        return temp
    
    def sort(self):
        list_out = [None] * self.max_in
        bw = self.max_in - 1
        fw = 0
        while bw != -1:
            if self.array[bw] != None:
                list_out[fw] = self.array[bw]
                fw += 1
            bw -= 1
            
        self.array = list_out
        print(self.array)
        
            
    def reverse(self):
        print(self.array)
        temp = [None] * self.max_in
        max_i = self.max_in - 1
        stop_index = 0
        beg = 0
        
        for i in range(self.max_in):
            if self.array[i] != None:
                stop_index += 1
                
        stop_index -= 1
        
        while stop_index > -1 :
            temp[stop_index] = self.array[beg]
            stop_index -= 1 
            beg += 1
            
        self.array = temp
        
    def copy(self):
        new_list = List(self.max_in)
        
        min_i = 0
        for i in range(self.max_in):
            new_list.append(self.array[i])
            min_i += 1
        return new_list
    
    def get_array(self):
        return self.array
    
 


# array = List(5)

# print("Array: ", end = " ")
# array.get_array()

# array.append(1)
# print("Array: ", end = " ")
# array.get_array()

# array.extend([5,6])
# print("Array: ", end = " ")
# array.get_array()

# array.insert(2, 10)
# print("Array: ", end = " ")
# array.get_array()

# array.remove(5)
# print("Array: ", end = " ")
# array.get_array()

# array.pop(0)
# print("Array: ", end = " ")
# array.get_array()

# # array.clear()
# # print("Array: ", end = " ")
# # array.get_array()

# print("Array Index: " + str(array.index(10)))

# print("\nFinal Array: ", end = " ")
# array.get_array()

a = List(10)
a.extend([100, 99, 88, 77, 66, 55, 44, 33, 22, 1])
a.sort()
assert a.get_array() == [1, 22, 33, 44, 55, 66, 77, 88, 99, 100]
a = List(12)
a.extend([100, 99, 88, 77, 66, 55, 44, 33, 22, 1])
a.sort()
assert a.get_array() == [1, 22, 33, 44, 55, 66, 77, 88, 99, 100, None, None]
