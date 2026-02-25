# absolute_file_path = "C:\\data\\github\\ua4593\\lessons\\lesson14\\data.txt"
# relative_file_path1 = "data.txt"
# relative_file_path2 = "lessons\\lesson14\\data.txt"
# # open_file = open(absolute_file_path)
# # open_file = open(relative_file_path)
# # print(open_file.read())
# # open_file.close()

# from funk import print_file_content
# print_file_content(absolute_file_path)
# # print_file_content(relative_file_path2)
# print_file_content(relative_file_path1)

# relative_file_path2 = "lessons\\lesson14\\data.txt"

# open(relative_file_path2, 'rt')
# output_file_path = "lessons\\lesson14\\output.txt"
# open(output_file_path, 'w')

# try:
#     file = open(relative_file_path2, 'rt')
# except FileNotFoundError:
#     print(f"File not found: {relative_file_path2}")
# finally:
#     print("Finished attempting to open the file.")
#     file.close()


# file_path = "lessons\\lesson14\\data.txt"
# file = open(file_path, 'r')
# text = file.read()
# print(f"pos: {file.tell()} text: {text}")
# file.seek(10)  # Move the file pointer back to the beginning of the file
# text = file.read(5)
# print(f"pos: {file.tell()} text: {text}")
# text = file.read(5)
# print(f"pos: {file.tell()} text: {text}")
# text = file.read(5)
# print(f"pos: {file.tell()} text: {text}")
# file.close()


# file = open(file_path, 'r')
# lines = file.readlines()
# print(lines)

# file = open(file_path, 'r')
# lines = file.readline()
# print(lines)
# lines = file.readline()
# print(lines)




# file = open(file_path, 'r')
# for index, line in enumerate(file):
#     print(f"Line {index + 1}: {line.strip()}")
# file.close()

# file = open("lessons\\lesson14\\data.txt", 'r')
# while True:
#     content = file.read(5)
#     if not content:
#         print(type(content), content)
#         break
#     print(content)

# file = open("lessons\\lesson14\\data.txt", 'r')
# while content := file.read(5):

#     print(content)

# with open("lessons\\lesson14\\data.txt", 'r') as aaa:
    # content = aaa.read()
    # print(content)

import datetime
with open("lessons\\lesson14\\output.txt", 'a') as file:
    date_time = datetime.datetime.now()
    content = file.write(f"Hello, world! {date_time}\n")
    print(content)
    list_of_numbers = [1, 2, 3, 4, 5]
    content = file.writelines(map(str, list_of_numbers))

