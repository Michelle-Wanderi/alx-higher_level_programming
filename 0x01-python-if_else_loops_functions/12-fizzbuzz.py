# #!/usr/bin/python3
# def fizzbuzz():
#     for i in range(1, 101):
#         if i % 3 == 0:
#             print('Fizz', end='')
#         if i % 5 == 0:
#             print('Buzz', end='')
#         if i % 3 != 0 and i % 5 != 0:
#             print(i, end='')
#         print(' ', end='')

def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    
    if n % 3 == 0 and n % 5 != 0:
        print('Fizz')

    if n % 5 == 0 and n % 3 != 0:
        print('Buzz')

print(fizzBuzz())
    