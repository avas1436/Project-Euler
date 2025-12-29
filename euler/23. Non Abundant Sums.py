import time


def abundant(num: int):
    total = 1
    if num % 2 == 0:
        total += 2 + (num / 2)

    for i in range(3, ((num // 3) + 1)):
        if num % i == 0:
            total += i
            if total > num:
                return True
    return False


# print(abundant(28))


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
    start_abundat = time.process_time()
    nums = abundant_tuple()
    end_abundat = time.process_time() - start_abundat
    print(f"Making abundant tuple take {end_abundat} seconds")

    start_answare = time.process_time()
    answare = solve(nums)
    end_answare = time.process_time() - start_answare
    print(f"Proccess Solve function in {end_answare} seconds")

    print(f"The answare is : {answare}")
