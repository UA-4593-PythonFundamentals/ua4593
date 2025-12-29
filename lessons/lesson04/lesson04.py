# i = 0
# print(f"Starting loop... {i=}" )
# while i < 5:
#     print("Iteration:", i, end=' ')
#     i += 1 
#     print(" - i incremented to:", i)

# print("Loop ended. Final value of i:", i)


# i = 0
# print(f"Starting loop... {i=}" )
# while i < 5:
#     print("Iteration:", i, end=' ')
#     i -= 1 
#     print(" - i incremented to:", i)

# print("Loop ended. Final value of i:", i)


# while True:
#     print("This loop will run forever unless interrupted.")
#     load_data()  # Hypothetical function to load data
#     process_data()  # Hypothetical function to process data
#     send_results()  # Hypothetical function to send results
#     import time
#     time.sleep(60*60*24)  # Sleep for 24 hours before next iteration

# is_false = [False, None, 0, "", [], {}, set()]

# # while len(is_false) > 0:
# while is_false:
#     print("This will print once, then the list will be emptied.")
#     element = is_false.pop()  # Remove the last element from the list
#     print(f"Removed element: {element}, \tRemaining list: {is_false}")

# value = None
# while not value:
#     print("Value is falsy, continuing the loop.")
#     value = input("Please enter number: ")
#     if value.isdigit():
#         value = int(value)
#     else:
#         print(f"That's not a valid number. Try again. {value=}")
#         value = None

# print(f"Thank you! You entered a valid number: {value}")

# for i in range(5):
#     print("Iteration:", i)
#     print("\tThis is inside the loop.")

# for i in 10: # This will raise a TypeError: 'int' object is not iterable
#     pass
# iterable = [[1, 2], "text", (1,2,3,4), {'key1': 'value1', "key2": "value2"}, {1,2,3,4,1,2,3,4}]
# print(f"Iterating over: {iterable}")
# for element in iterable:
#     print(f"Current element: {element}")
#     for item in element:
#         print(f"\tItem: {item}")
# print("Iteration complete.")

# print(f"{item=}") 

# l = [1, 2, 3, 4, 5, [1,2,3]]
# for element in l:
#     print(f"Current element: {element}", end=' ')
#     if isinstance(element, list):
#         element.append(len(element))
#     else:
#         element = element * 10
#     print(f"\tModified element inside loop: {element}")
# print("List after loop:", l)


# r = range(5)
# print(f"Range object: {r}, converting to list: {list(r)}")
# r = range(-5)
# print(f"Range object: {r}, converting to list: {list(r)}")
# r = range(-5, 0)
# print(f"Range object: {r}, converting to list: {list(r)}")
# r = range(-5, 15, 3)
# print(f"Range object: {r}, converting to list: {list(r)}")
# for i in r:
#     print(f"{i}", end=' => ')
# print()

# l = [1, 2, 3, 4, 5, [1,2,3]]
# for i in range(len(l)):
#     print(f"Current element: {l[i]}", end=' ')
#     if isinstance(l[i], list):
#         l[i].append(len(l[i]))
#     else:
#         l[i] = l[i] * 10
#     print(f"\tModified element inside loop: {l[i]}")
# print("List after loop:", l)

# col=[10, 20, 30, 40, 50]
# e = enumerate(col)
# print(f"{e}, converting to list: {list(e)}")
# col="text"
# e = enumerate(col)
# print(f"{e}, converting to list: {list(e)}")
# col=(1,2,3,4,5)
# e = enumerate(col)
# print(f"{e}, converting to list: {list(e)}")
# col={"key1": "value1", "key2": "value2"}
# e = enumerate(col)
# print(f"{e}, converting to list: {list(e)}")

# l = [1, 2, 3, 4, 5, [1,2,3]]
# for pair in enumerate(l):
#     print(f"Current element: {pair}")
#     if isinstance(l[pair[0]], list):
#         l[pair[0]].append(len(l[pair[0]]))
#     else:
#         l[pair[0]] = pair[1] * 10
#     print(f"\tModified element inside loop: {l[pair[0]]}")
# print("List after loop:", l)

# a, b = 10, 20
# print(f"Before swap: a={a}, b={b}")
# a, b , c= (b, a, a+b)
# print(f"After swap: a={a}, b={b}, c={c}")

# l = [1, 2, 3, 4, 5, [1,2,3]]
# for i, value in enumerate(l):
#     print(f"Current element: {(i, value)}")
#     if isinstance(value, list):
#         l[i].append(len(value))
#     else:
#         l[i] = value * 10
#     print(f"\tModified element inside loop: {l[i]}")
# print("List after loop:", l)

# d = {
#     'key1': 'value1', 
#     'key2': 'value2', 
#     'key3': [1,2,3]
# }
# for key in d:
#     print(f"Current key: {key}, value: {d[key]}")
#     if isinstance(d[key], list):
#         d[key].append(len(d[key]))
#     else:
#         d[key] = d[key] + "_modified"
#     print(f"\tModified value inside loop: {d[key]}")
# for key, value in d.items():
#     print(f"Final key-value pair: {key}: {value}")
#     if isinstance(value, list):
#         value.append(len(value))
#     else:
#         d[key] = value + "_finalized"
#     print(f"\tFinalized value inside loop: {d[key]}")

# from pprint import pprint
# print("Dictionary after loop:")
# pprint(d)


# break/continue

# while True:
#     user_input = input("Enter 'exit' to break the loop or 'skip' to continue: ")
#     if user_input.lower() == 'exit':
#         print("\tBreaking the loop.")
#         break
#     elif user_input.lower() == 'skip':
#         print("\tContinuing to next iteration.")
#         continue
#     print(f"You entered: {user_input}")
#     print("Processing your input...")

# l = [1, 2, 3, "text", 6, 7,[ 8, 9], 10]

# suma = 0
# for element in l:
#     if not isinstance(element, int):
#         print(f"Non-integer element found: {element}, skipping...")
#         continue

#     if element > 7:
#         print(f"Element {element} is greater than 7, breaking the loop.")
#         break
#     suma += element
#     print(f"Added {element} to sum, current sum: {suma}")
# else:
#     print("Loop completed without encountering a break.")
# print(f"Final sum of integers less than or equal to 7: {suma}")

# l = [1, 2, 3, "text", 6, 5,[ 8, 9], 3]

# suma = 0
# for element in l:
#     if not isinstance(element, int):
#         print(f"Non-integer element found: {element}, skipping...")
#         continue

#     if element > 7:
#         print(f"Element {element} is greater than 7, breaking the loop.")
#         break
#     suma += element
#     print(f"Added {element} to sum, current sum: {suma}")
# else:
#     print("Loop completed without encountering a break.")
# print(f"Final sum of integers less than or equal to 7: {suma}")

# l = [1, 2, 3, 5, 6, 5, +3, 3]
# contain_negative = False
# for element in l:
#     if element < 0:
#         print(f"Negative element found: {element}, breaking the loop.")
#         contain_negative = True
#         break
#     print(f"Current element: {element}, continuing...")

# if not contain_negative:
#     print("No negative elements found in the list.")



# for element in l:
#     if element < 0:
#         print(f"Negative element found: {element}, breaking the loop.")
#         break
#     print(f"Current element: {element}, continuing...")
# else:
#     print("No negative elements found in the list.")

# tetx = "This is a sample text for testing."
# for char in tetx:
#     pass
#     # if char in "aeiou":
#     #     print(f"Vowel '{char}' found, breaking the loop.")
#     #     break
#     # print(f"Current character: '{char}', continuing...")

# i = 0
# while i < 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# for x in range(101):
#     if x % 2 == 0:
#         print (x)
# for x in range(0, 101, 2):
#     print (x)

# for x in range(1, 100, 2):
#     print (x, end=' ')
# print()
# for x in range(100):
#     if x % 2 == False:
#         continue
#     print (x, end=' ')
# print()

random_numbers = [
    [12, 7, 5, 20, 33, 8, 15, 3, 27, 10],
    [2, 4, 6, 8, 10, 12],
    [11, 13, 15, 17],
    [0, -2, -4, -6],
    [14, 16, 18, 19]
]
for sublist in random_numbers:
    print(f"Checking sublist: {sublist}")
    for number in sublist:
        if number % 2: #  number % 2 == 1
            print(f"\tFirst odd number found: {number}")
            break
    else:
        print("\tNo odd numbers found in this sublist.")

# for number in random_numbers:
#     if number % 2:
#         print(f"First odd number found: {number}")
#         break
# else:
#     print("No odd numbers found in the list.")