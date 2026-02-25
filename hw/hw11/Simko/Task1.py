def check_age(age):
       if age < 0:
              raise ValueError("Age can`t be negative")
       if age % 2 == 0: 
              return("You input age even") 
       else: 
              return("You input age odd")
try:
        age = int(input("Enter your age: "))
        result = check_age(age)
        print(result)
except ValueError as e:
        print(e)
       
