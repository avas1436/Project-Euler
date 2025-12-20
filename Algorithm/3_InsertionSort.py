from rich import print


def insertionsort(head: list):
    for i, num in enumerate(head):
        limit = i + 1
        step = 0
        while step < limit:
            if num < head[step]:
                head[i], head[step] = head[step], head[i]
                print(f"[red]{head}[/red]")
            step += 1

    print(f"[blue]{head}[/blue]")


insertionsort(head=[4, 2, 3, 5, 1])
