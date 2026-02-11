def solution(number):
    if number <= 0:
        return 0

    total = 0
    for a in range(number):
        if a % 3 == 0 or a % 5 == 0:
            total += a
    return total