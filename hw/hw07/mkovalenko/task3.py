def number_of_characters(input_string):
    my_dict = {}
    for c in input_string:    
        my_dict.update({c: input_string.count(c)})
    return my_dict

my_string = input("Type string: ")
print("result:", number_of_characters(my_string))