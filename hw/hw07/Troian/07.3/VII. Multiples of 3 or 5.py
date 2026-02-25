def solution(number):
    res = 0
    if(number > 0):
        return sum(i for i in range(number) if (i % 3 == 0 or i % 5 == 0))
    return 0