for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
number_stars = int(input("Number of stars:"))
for i in range(number_stars):
    print("*", end="")
# d

numbers = int(input("\nNumber of stars: "))
for i in range(1, numbers+1):
    print("*" * i)