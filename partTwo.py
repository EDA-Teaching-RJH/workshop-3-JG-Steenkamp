import random
secret_number = random.randint(1, 10)
guess_amount = 0
guess_limit = 3 
while guess_amount < guess_limit :
    guess = int(input("guess:"))
    guess_amount += 1
    if guess == secret_number:
        print("well done!")
        break
else:
    print("you lose!")