import math

# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

# Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(dist, 2)

#No yelling!
def filter_words(st):
    words = st.split()
    cleaned_string = " ".join(words)
    return cleaned_string.capitalize()

#Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Reversing Words in a String
def reverse_words(st):
    return " ".join(st.split()[::-1])

#Reverse List Order
def reverse_list(l):
    return l[::-1]

#Multiples of 3 or 5
def solution(number):
    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

#Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

#Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)

#Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail