class Human:
     def __init__(self, name):
       self.name = name

     def welcom_message(self):
          return(f"Hello {self.name}")

     def species(self):
          return  "HomoSapiens"
    
     @staticmethod
     def static_method():
          return "Arbitrary Message"
human = Human("John")
print(human.welcom_message())
print(human.species())
print(human.static_method())