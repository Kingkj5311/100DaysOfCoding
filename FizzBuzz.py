# Completed

for x in range(1,101):
    if x % 5 != 0 and x % 3 != 0:
        print(x)
    else:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        if x % 3 == 0:
            print("Fizz")
        if x % 5 == 0:
            print("Buzz")

# ==========================================================================================
# Refined 

for x in range(1,101):
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)