# Completed

def prime_checker(number):
    p=0
    for x in range (2,number):
        if x != number:
            if number % x == 0:
                p=1
    if p == 0:
        print(f"It's a prime number. {number}")
    else:
        print(f"It's not a prime number. {number}")
for i in range(1,101):
    prime_checker(i)