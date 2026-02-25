def depending_on_the_number_day(number):
       days = {
               1: "Monday",
               2: "Tuesday",
               3: "Wednesday",
               4: "Thursday",
               5: "Friday",
               6: "Saturday",
               7: "Sunday"
       }
       
       if number not  in days:
               raise  ValueError("Number must be between 1 and 7")
       return  days[number]

try:
        number = int(input("Enter a number between 1 and 7: "))
        day = depending_on_the_number_day(number)
        print(depending_on_the_number_day(number))
except ValueError as e:
        print(e)
              
