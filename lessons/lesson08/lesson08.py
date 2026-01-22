# import math


# print("Lesson 08: Math Module")
# print(math.sqrt(16))
# print(math.pi)

# from math import sqrt, pi

# print(sqrt(25))
# print(pi)

# import sys
# from pprint import pprint
# pprint(sys.path)

# import constants
# print(constants.get_lesson_info())
# print(constants.NAME)

# sys.path.append('c:\\data\\github\\ua4593\\lessons\\lesson07')
# pprint(sys.path)

# import lesson07
# print(lesson07.l)

# import math, random, datetime, sys
# from math import factorial, pi, sqrt

# before = dir()
# print(f"Before import: {before}\n")

# from constants import *

# after = dir()
# print(f"After import: {after}\n")

# print("defference:", set(after) - set(before))

# print(f"\nLesson Name: {NAME}")
# print(f"Description: {DESCRIPTION}")

# import constants_copy
# import constants

# print(constants_copy.get_lesson_info())
# print(constants.get_lesson_info())

# from constants_copy import get_lesson_info as get_lesson_info_copy
# print(get_lesson_info_copy())
# from constants import get_lesson_info
# print(get_lesson_info())

# from constants_copy import NAME as COPY_NAME, DESCRIPTION, DURATION, LEVEL, AUTHOR as COPY_AUTHOR, get_lesson_info

# print(f"Lesson Name: {COPY_NAME}")
# print(f"Description: {DESCRIPTION}")
# print(f"Duration: {DURATION} minutes")
# print(f"Level: {LEVEL}")
# print(f"Author: {COPY_AUTHOR}")
# print("Lesson Info:", get_lesson_info())

# import ex
# print(f"{__name__=}")
# ex.print_lesson_details()


# from l1.info import print_info as print_info_l1
# from l1.l2.info import print_info as print_info_l2
# from l1.l2.l3.info import print_info as print_info_l3

# print_info_l1()
# print_info_l2()
# print_info_l3()

# import l1
# l1.print_info()

# from l1.l2.l3.info import print_info as print_info_l3



before = dir()
print(f"Before import: {before}\n")

# from myall import *
from myall import _age, get_profile, country, Name
after = dir()
print(f"After import: {after}\n")

print("defference:", set(after) - set(before))
print(f"{ get_profile()}")