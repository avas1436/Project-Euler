def insertionsort(head: list):
    sorted_list = []
    sorted_list.append(head.pop())
    print(sorted_list)
    for _ in range(len(head)):
        steps = 0
        limit = len(sorted_list)
        current = head.pop()
        ind = 0
        while steps < limit:
            print(f"sefr : {steps}")
            if sorted_list[steps] < current:
                ind = steps + 1
                print(f"paeen : {ind}")
            else:
                ind = steps
                print(f"bala : {ind}")

            steps += 1

        sorted_list.insert(ind, current)
        print(f"[red]{sorted_list}[/red]")

    print(f"[blue]{sorted_list}[/blue]")


insertionsort(head=[4, 2, 3, 5, 1])
