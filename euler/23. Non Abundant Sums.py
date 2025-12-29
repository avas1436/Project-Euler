def abundant(num: int):
    divisors = set()
    for i in range(1, ((num // 2) + 1)):
        if num % i == 0:
            divisors.add(i)
        print(f"for i = {i}, divisors : {divisors}")

    return sum(divisors)


print(abundant(12))
