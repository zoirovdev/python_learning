# # if statement
# x = int(input('Enter an integer: '))
# if x<0:
#     print('Integer is not less than zero')
# elif x==0:
#     print('Integer is zero')
# else:
#     print('Integer is bigger than zero')


# for statement
# words = ['cat', 'window', 'defenestrate']
# for word in words:
#     print(word, len(word))


# creating a sample collection
# cars = {'Lamborghini':'huracan', 'Lamborghini':'aventador', 'Bugatti':'chiron'}

# # iterate over a copy
# for car, model in cars.copy().items():
#     if(model == 'chiron'):
#         del cars[car]

# print(cars)


# range() function
# for i in range(5):
#     print(i)

# print(list(range(10)))
# print(list(range(8, 88)))
# print(list(range(-10, -100, -1000)))


# a = ['Mary', 'had', 'a', 'red', 'dress']
# for i in range(len(a)):
#     print(a[i])

# print(sum(range(4)))

# for a in range(2, 10):
#     for b in range(2, a):
#         if a % b == 0:
#             print(f"{a} equals {b} * {a//b}")
#             break


# for num in range(2, 10):
#     if num % 2 == 0:
#         print(f"{num} is even number")
#         continue
#     print(f"{num} is odd number")


# for a in range(2, 10):
#     for x in range(2, a):
#         if a % x == 0:
#             print(a, 'equals', x, '*', a//x)
#             break
#     else:
#         print(a, 'is a prime number')



# pass statement
# while True:
#     pass

# if True:
#     pass

# class MyEmptyClass:
#     pass

# def initlog():
#     pass



# def http_eror(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "here is teapot"
#         case _:
#             return "something went wrong"
        
# print(http_eror(400))



# defining functions
# def fib(n):
#     """Print Fibonacci series less than n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()

# fib(2000)
# f = fib
# f(1000)


# def fib2(n):
#     """Return fibonacci series less than n."""
#     series = []
#     a, b = 0, 1
#     while a < n:
#         series.append(a)
#         a, b = b, a + b
#     return series

# print(fib2(3000))



# def ask_ok(prompt, retries=4, reminder="Please try again"):
#     while True:
#         reply = input(prompt)
#         if reply in ['y', 'ye', 'yes', 'yeah', 'yep']:
#             return True
#         elif reply in ['n', 'no', 'not', 'nope']:
#             return False
#         retries -= 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

    
# print(ask_ok("Is it right?"))

        

