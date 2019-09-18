#Challenge #4: Reverse the vowels in a string. For example, "Marry Me" --> Merry Ma, a and e are switched

list_user = list(input("Write a string:" ))
list_output = []
set_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowels = []
index = 0

for i in list_user:
  if(i in set_vowels):
    vowels.append(i)

vowels = vowels[::-1]

for i in list_user:
  if(i in set_vowels):
    list_output.append(vowels[index])
    index += 1
  else:
    list_output.append(i)

print("".join(list_output))
