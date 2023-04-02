# Question 1
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print("Your name is", name)

# Question 3
in_file = open("numbers.txt", "r")
num1 = int(in_file.readline())
num2 = int(in_file.readline())
in_file.close()
result = num1 + num2
print(result)

#  Question 4
in_file = open("numbers.txt", "r")
total_lines = 0
for line in in_file:
    number = int(line)
    total_lines += number
in_file.close()
print(total_lines)
