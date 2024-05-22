# Targeting without loops
# Completed

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# position = "A2"

xaxis=position[0]
yaxis=position[1]

if xaxis=="A":
  column=1
if xaxis=="B":
  column=2
if xaxis=="C":
  column=3

row=int(yaxis)

if row == 1:
  line=line1
if row == 2:
  line=line2
if row == 3:
  line=line3

line[column-1]=" X"
print("    A\t  B\tC")
print(f"1 {line1}\n2 {line2}\n3 {line3}")


# =============================================================================================
# Clean uncommented code
# Refined
'''
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")
'''