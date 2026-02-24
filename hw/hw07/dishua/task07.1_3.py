string = input("Enter string: ")

def calculate_number_of_chars(str):
    chars = {}
    for char in str:
        if char in chars:
            chars[char]+=1
        else:
            chars.update({char:1})
    print(chars)

if __name__ == "__main__":
    calculate_number_of_chars(string)
