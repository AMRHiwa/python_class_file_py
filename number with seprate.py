'''
value  = int(input("Enter your number: "))
print(f'{value:,}' )
'''

# getting number
x = input("Enter your number : ")

# define the counter for conting numbers
counter = 0

# define the empty string as s for saving the new number
s=''


for i in x[::-1]:
    if counter%3 == 0 and counter != 0:
        s = s + ','
    s = s+i 
    counter += 1

print(s[::-1])