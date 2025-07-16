nums_row = int(input("Enter the size of the pattern: "))
i = 0
while i < nums_row:
    for j in range(nums_row):
        print("*", end="")
    print()
    i += 1   