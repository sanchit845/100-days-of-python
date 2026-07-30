from random import randint

c = randint(1, 100)

n = int(input("Enter a number between 1 and 100: "))

guesses = 0

while True:
    guesses +=1
    if n< c:
        print("Try Higher!")
        n = int(input("Enter a number between 1 and 100: "))
    elif n > c:
        print("Try Lower!")
        n = int(input("Enter a number between 1 and 100: "))
    else:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break