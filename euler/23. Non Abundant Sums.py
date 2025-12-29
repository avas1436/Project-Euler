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


def abundant_set(start: int = 1, end: int = 28124):
    abundant_ls = set()
    for i in range(start, end):
        if abundant(i):
            abundant_ls.add(i)
    return abundant_ls


n = abundant_set()
print(n)
