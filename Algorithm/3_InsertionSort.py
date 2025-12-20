def insertionsort(head: list):
    sorted_list = []
    for _ in range(len(head)):
        limit = len(sorted_list)
        current = head.pop()

        if limit == 0:
            sorted_list.append(current)
            print(f"[red]{sorted_list}[/red]")

        if limit == 1:
            if sorted_list[0] < current:
                sorted_list.append(current)
                print(f"[red]{sorted_list}[/red]")
            else:
                sorted_list.insert(0, current)
                print(f"[red]{sorted_list}[/red]")

        if limit == 2:
            if sorted_list[1] <= current:
                sorted_list.append(current)
                print(f"[red]{sorted_list}[/red]")
            if sorted_list[0] <= current <= sorted_list[1]:
                sorted_list.insert(1, current)
                print(f"[red]{sorted_list}[/red]")
            else:
                sorted_list.append(current)
                print(f"[red]{sorted_list}[/red]")

        else:
            for j in range(1, limit - 2):
                if sorted_list[j - 1] <= current <= sorted_list[j + 1]:
                    sorted_list.insert(j, current)
                    print(f"[red]{sorted_list}[/red]")
                elif sorted_list[j - 1] <= current:
                    sorted_list.insert(j - 1, current)
                    print(f"[red]{sorted_list}[/red]")
                elif current <= sorted_list[j + 1]:
                    sorted_list.insert(j + 1, current)
                    print(f"[red]{sorted_list}[/red]")

    print(f"[blue]{sorted_list}[/blue]")


insertionsort(head=[4, 2, 3, 5, 1])
