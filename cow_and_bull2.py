import random

def getDigits(num):
    return [int(i) for i in str(num)]

def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False
    
def generateNum():
    while True:
        num = random.randint(10,99)
        if noDuplicates(num):
            return num

def numofBullsAndCow(num, guess):
    bull_cows = [0,0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i,j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cows[0] += 1
            else:
                bull_cows[1] += 1
    
    return bull_cows

num = generateNum()
tries = int(input("Enter number of tries, You want to give: "))

while tries > 0:
    guess = int(input("Enter your guess:"))
    if not noDuplicates(guess):
        print("No digit cannot be repeated !!")
        continue

    if guess<10 or guess>99:
        print("Number should be of two(2) digit !!")
        continue

    bullCows = numofBullsAndCow(num, guess)
    print("Bulls :", bullCows[0])
    print("Cows :", bullCows[1])
    tries -= 1

    if bullCows[0] == 2:
        print(f"You won !!, You Guessed right. The number was {num}. Thanks for playing.")
        break

else:
    print(f'You ran out of tries !! The number was {num}')

    

''' bull_cows = numofBullsAndCow(num, guess)
    print("Bulls :", bull_cows[0])
    print("Cows :", bull_cows[1])
    tries -= 1 '''


