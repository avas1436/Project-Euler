from rich import print

# my_list = [3, 5, 8, 4]
my_list = [4, 2, 3, 5, 1]

swapped = True
limit = len(my_list) - 1
counter = 0


while swapped == True:
    swapped = False
    for i in range(limit):
        if my_list[i + 1] < my_list[i]:
            hold = my_list[i + 1]
            my_list[i + 1] = my_list[i]
            my_list[i] = hold
            swapped = True
            print(f"[red]{my_list}[/red]")
        else:
            print(f"[blue]{my_list}[/blue]")

        counter += 1
    limit -= 1

print(counter)
print(f"[green]{my_list}[/green]")
