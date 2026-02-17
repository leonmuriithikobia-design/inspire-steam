#Leon Kobia
#17/02/26
#Program to display diamond and triangle using *
rows = 5

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
rows = 5

# Top half
for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Bottom half
for i in range(rows - 1, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
