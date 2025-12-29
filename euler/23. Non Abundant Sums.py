def abundant(num: int):
    total = 0
    for i in range(1, ((num // 2) + 1)):
        if num % i == 0:
            total += i
            if total > num:
                return True
    return False


# print(abundant(12))


def abundant_tuple(start: int = 1, end: int = 28124):
    abundant_ls = []
    for i in range(start, end):
        if abundant(i):
            abundant_ls.append(i)
    return tuple(abundant_ls)


# n = abundant_tuple()
# print(n)


def solve(num_set: set):
    nums = {i: True for i in range(1, 28124)}
    for i, num_1 in enumerate(num_set):
        for num_2 in num_set[i:]:
            sum = num_1 + num_2
            if sum > 28123:
                break
            if nums[sum]:
                nums[sum] = False
    total = 0
    for k, boo in nums.items():
        if boo:
            total += k

    return total


if __name__ == "__main__":
    nums = abundant_tuple()
    answare = solve(nums)
    print(answare)
