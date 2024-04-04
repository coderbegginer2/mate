import random
enter_name = input("hello my fellow friend.what's your name? ") #entering name
print("hello " + enter_name + ".I am guessing a random number from 1 to 10 can you guess it? you have 5 attempts ")#greeting the player.
attempt = 1
# prints a random value from the list and stores it in memory
list = [1, 2, 3, 4, 5, 6, 7 ,8 ,9 ,10]
Random= random.choice(list)
while attempt < 5:
    guessing_number = int(input("what's your number? ") )                                        #guessing the number
    if Random == guessing_number:
        print("you are rite and i hate you :(  ")
        print("number of attempts :"+str(attempt) )
        break
    elif Random > guessing_number:
        print("No,your number is lower than my guess ")
        attempt +=1
    elif Random < guessing_number:
        print("your guess is higher")  
        attempt +=1  
if attempt < 5:
    print("mission accomplished")
else:
    print("mission Failed we will get him next time")
    print(Random)