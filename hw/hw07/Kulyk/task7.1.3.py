def character (word):
  """ This function calculates the number of characters"""
  counts = {}
  for i in word:
      if i in counts:
        counts[i] += 1 
      else:
        counts[i] = 1 
  return counts

word = input("Enter a word: ").lower() 
print (character(word))
