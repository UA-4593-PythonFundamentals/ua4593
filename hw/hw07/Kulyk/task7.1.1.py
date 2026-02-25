def num (a, b):
  """This function returns the largest number"""
  if (a > b):
    result = a
  elif (b > a):
    result = b
  elif (a == b):
    result = "Equal"
  return result

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(num(a, b))