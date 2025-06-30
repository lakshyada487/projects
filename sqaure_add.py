num = int(input("enter an integer: "))
total = 0
for i in range(1, num+1):
    square = i ** 2
    print(square)
    total += square
print("total is", total)

#taking input from user, squaring it and then adding the sqaures and just printing the total number

#this is for astericks

for i in range(1,25):
    print("* " * i, i)
