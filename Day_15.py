from random import randint

c = randint(1, 100)

guesses = 0

while True:
    guesses +=1
    n = int(input("Enter a number between 1 and 100: "))
    if n< c:
        print("Try Higher!")
    elif n > c:
        print("Try Lower!")
    else:
        print(f"Congratulations! You guessed the number {n} in {guesses} guesses.")
        break