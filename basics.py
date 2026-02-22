# Today I started learning python (date: Sun 22 Feb 2026)
# Topics I/O, numbers, text and using python as a calculator

### I/O
name=input("Enter your name: ")
print(name)

### numbers
n=12
m=23.45
print(n, m)
print(n * m) # multiplication
print(n / m) # division
print(n ** m) # evaluating mth power of n
print(n + m) # addition
print(n - m) # subtraction


### text
# defining string variables
surname="Ritchie"
laptop="MacBook Pro"
car="Bentley"

print(laptop[1]) # getting character from string by its index
print(car[:3]) # slicing
print(len(surname)) # built-in len function

### fibonaci sequence
a, b = 0, 1
while a < 10:
    print(a)
    a,b=b,a+b




