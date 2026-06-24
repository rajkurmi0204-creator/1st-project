import random

number=random.randint(1,100)

count=0
while count>0:      # infinite loop
    count+=1
    user=int(input('enter your number'))
    if user==number:
        print(f"you won man")
        print(f"you took {count} to win")
        break
    elif user<number:
        print(f"too low value guess high")
    elif user>number:
        print(f"too high value guess lower value")


#user have only 5 chance and if those chances are over either he will win or loss

  
        