
# question1: write a code show all multiple of 4 from 1 to 10
for i in range(1, 11): # 1 2 3 4 ... 9 10
    print( 4 * i )

# level 1: i=1
# >> 4 * i -> 4

# level 2: i=2
# >> 4 * i = 4 * 2 -> 8

# level 3: i=3
# >> 4 * i = 4 * 3 -> 12

# ...

# level 10: i=10
# >> 4 * i = 4 * 10 -> 40






# question2: write a code that take a number from user and show 0 to number

# take a number from user
number = int(input("Enter your number: "))

# define the for loop 
for i in range(number + 1):
    print(i, end=', ')
 
    
 
    
 
    
 
# question3: write a program that take five numbers and calculate sum of them
# way1 by loop
sum1 = 0

for i in range(5):
    a = int(input("Enter your number : "))
    sum1 += a

print(sum1)

# way2 without loop
a, b, c, d, e = map(int, input("Enter five numbers: ").split())

temp = sum([a, b, c, d, e])

print(temp)



 
# question4: write a program that take a number and show multiple of 5 from 1 
# to our number

# take a number from user
num = int(input("Enter your number: "))

# calculat of multiple of 5
for i in range(1, num+1):
    print(5 * i)





# question5 : write a code that take x and n then calculate below formula  
# x^1 + x^2 + x^3 + ... + x^n
n, x = map(int, input("Enter n and x : ").split() )

sum_ = 0

for i in range(1, n+1):
    sum_ += x**i

print(sum_)







