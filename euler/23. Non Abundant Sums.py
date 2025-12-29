def abundant(num: int):
    divisors = set()
    for i in range(1, ((num // 2) + 1)):
        if num % i == 0:
            divisors.add(i)

    total = sum(divisors)
    if total >= num:
        return total
    else:
        return False


# print(abundant(12))
#
#
