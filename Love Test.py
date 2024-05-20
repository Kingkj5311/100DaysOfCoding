print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# Concatonate the two names
name = name1 + name2
# Ensure the name is in lowercase
name = name.lower()
# Check for the occurence of the letters in the word "true" and "love"
x=name.count("t")
x+=name.count("r")
x+=name.count("u")
x+=name.count("e")
y=name.count("l")
y+=name.count("o")
y+=name.count("v")
y+=name.count("e")
# Concatonate the two numbers
string=str(x)+str(y)
# Output the result
print(int(string))
# Interpretation of the result
if value >=40 and value <=50:
    print(f"Your score is {value}, you are alright together.")
else:
    if value < 10 or value >90:
        print(f"Your score is {value}, you go together like coke and mentos.")
    else:
        print(f"Your score is {value}.")
# ================================================================================================
"""
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
"""