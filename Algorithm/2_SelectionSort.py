from rich import print


def selection_sort(head: list):
    limit = len(head)
    counter = 0
    start = 0
    while start < limit:
        temp = start
        for i in range(start + 1, limit):
            if head[i] < head[temp]:
                temp = i

        head[start], head[temp] = head[temp], head[start]

        print(f"[red]{head}[/red]")

        counter += 1
        start += 1

    print(f"[green]{head}[/green]")
    print(f"Number of steps is :[blue]{counter}[/blue]")


selection_sort(head=[4, 2, 3, 5, 1])
