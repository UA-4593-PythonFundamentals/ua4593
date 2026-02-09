#I.Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

#II.Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    # Your code here
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return round(distance, 2)

#III. No yelling!
def filter_words(st):
    pass 
    cleaned = " ".join(st.split()).lower()
    return cleaned.capitalize()

#IV. Convert a Number to a String
def number_to_string(num):
    pass # Return a string of the number here!
    return str(num)

#V.Reversing Words in a String
def reverse(st):
    # Your Code Here
       words = st.split()
       reversed_words = words[:: -1]
       return " ".join(reversed_words)

#VI. Reverse List Order
def reverse_list(l):
    'return a list with the reverse order of l'
    return l [:: -1]

#VII. Multiples of 3 or 5
def solution(number):
  pass
  if number < 0: 
     return 0
  return sum(i for  i in range(number) if i % 3 == 0 or i % 5 == 0)

#VIII.Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;
   if distance_to_pump <= mpg * fuel_left:
      return True
   else:
      return False

#IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
  # Implement me!
  if name[0] == "R" or name[0] == "r":
      return name + " plays banjo"
  else:
      return name + " does not play banjo"

#X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
   # TODO
   if boolean:
      return "Yes"
   else:
      return "No"

#XI. Counting sheep
def count_sheeps(sheep):
  # TODO May the force be with you
  return sum(1 for s in sheep if s)

sheep = [True,  True,  True,  False,
            True,  True,  True,  True ,
            True,  False, True,  False,
            True,  False, False, True ,
            True,  True,  True,  True ,
            False, False, True,  True] 

#XII. Is this my tail?
def correct_tail(body, tail):
    return body[-len(tail):] == tail




