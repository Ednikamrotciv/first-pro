from random import randint
randVal=randint(0,100)
while(True):
    guess=int(input('please enter your guess: '))
    if guess == randVal:
        break
    elif guess <randVal:
        print('your guess was too low')
    else:
        print('too high')
print('you guess correctly',guess)
