# This is a program for writing lessons scores in a file that names 'score.txt'.
# Author: MDK
# Date: 1400/04/15 19:05
# ------------------------

print("Hello")
print("Welcome to calculating scores program!")
name = input("What's the student's name = ")  # This variable gets the name of student.
while name == "" or name == None:  # This 'while' checks that 'name' is empty or not. If 'name' was empty, program asks the name again.
    print("\nPlease enter the name!")
    name = input("What's the student's name = ")
    if name != "" and name != None:
        break
lessonsNumber = int(input("How many lessons do you want to write their scores = "))  # Lessons number wrote here.
with open('score.txt', 'w') as f:  # This line opens 'score.txt' for writing('w').
    f.write(f"{name} has scored :\n")
for i in range(0, lessonsNumber) :
    lessonName = input("\nPlease enter the name of lesson = ")  # This variable gets the name of lesson.
    score = input(f"Please enter the score of {lessonName} = ")  # This variable gets the score of lesson.
    with open('score.txt', 'a') as f:  # This line opens 'score.txt' for appending('a').
        if i == lessonsNumber - 1:  # This line checks that 'i' is in the end of file(score.txt) or not.
            f.write(f'{lessonName} : {score}')
        else:  # This line runs while 'i' is not in the end of file(score.txt).
            f.write(f'{lessonName} : {score}\n')

print("\nScores has been saved in 'score.txt' file")
print("Thanks for using this program")
