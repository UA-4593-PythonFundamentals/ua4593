def count_sheeps(sheep):
    counter = 0 
    for i in sheep:
        if(isinstance(i,bool)):
            if(i == True):
                counter += 1
    return counter



print(count_sheeps([True,True,True,False,True,False]))