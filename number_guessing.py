import random


num = random.randint(1,10)
correct_num = num
print("Hey! Lets play a Number Guessing Game.")
print("I am thinking of a number between 1 to 10")


user_input = int(input("Enter your guess:"))


if correct_num == user_input:
    print("Congrats! You have gussed it right. ")

elif user_input < correct_num :
    print("Your guess is very low") 

elif user_input > correct_num:
    print("Your guess is very high ")   
    
else:
    print("Invalid Input")
    
