#Switch the upper/lower case in a sentence containing strings. If the code is "HeLlo", it will print "hElLO.

string_sentence = input("Type a sentence: ")
string_sentence_new = []

for letter in string_sentence:
  if(letter.isalpha()):
    if(ord(letter) <= 90):
      string_sentence_new.append(letter.lower())
    else:
      string_sentence_new.append(letter.upper())
  else:
    string_sentence_new.append(letter)

print("".join(string_sentence_new))

#Algorithm: (1) Ask user to type a sentence. (2) For every character in the string, check to see if it's a letter -- use either is.alpha() or ASCII digists for upper and lower case. (3) If it is a letter, then convert it properly and then add it to the string. If it is not a letter, then add it as it is to the string. (4) Print the end string

#Note to Gabe: I converted upper/lower in class. So, I'm using the given function of Python since I was able to solve that problem already. For the .isalpha() function, I could instead use the ASCII values (eg. if ord(letter) is >= 65 and ord(letter) <=90)
