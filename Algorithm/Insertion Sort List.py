def insertionsort(head: list):
    for i in range(1, len(head)):
        key = head[i]
        j = i - 1
        while j >= 0 and head[j] > key:
            head[j + 1] = head[j]
            print(head)
            j -= 1
        head[j + 1] = key
        print(head)


insertionsort(head=[4, 2, 1, 3])
