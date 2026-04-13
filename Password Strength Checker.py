import time

password = input("Choose your password: ")
score = 0
numSpaces = 0
specialChars = ['$', '!', '@', '#', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', ':', ';', '<', '>', '.', '?', '/', '{', '}', '[', ']', '|']

print("Analyzing password")
for char in password:
    if char.isalpha:
        score += 0
    if char.isspace():
        score += .5
        numSpaces += 1
    if char.isupper():
        score += 1
    if char.isnumeric():
        score += 2
    if char in specialChars:
        score += 3
        print(char + " is a special character. These are very important when creating strong password!")

print("There were " + str(numSpaces) + " spaces in this password")
print("Your score is " + str(score) + " points")

time.sleep(3)
print()
if score > 20:
    print("This is an extremely secure password.")
    print("Click play to try with a new password.")
if 10 <= score <= 20:
    print("You could make this password more secure. Restart the program and try again.")
if score < 10:
    print("This password is extremely weak. Restart the program and try again.")