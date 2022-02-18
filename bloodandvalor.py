import sys
import time

print()
print()
print("#################################")
print("#                               #")
print("#         Blood and Dust        #")
print("#                               #")
print("##################################")
print("A Historical Fiction text based adventure game by Deepinder GIll.")

a = 2
b = 0.2
c = 0.4


def introduction():
    print()
    print("It is cold outside.")
    time.sleep(a)
    print("You begin to wonder if your mission will not be completed.")
    time.sleep(a)
    print("Ever since the Nazis have been in power, all of Europe has been a firestorm.")
    time.sleep(a)
    print("The provisional German Government have also been treating the local Norweigans poorly.")
    time.sleep(a)
    print("It is crucial that the message you are holding will get to the Commander")
    time.sleep(a)
    print("As these plans have the capability to turn the tide of the war.")
    time.sleep(a)
    print("Three paths emerge from the snowy weather, you wonder which one leads to the front lines.")
    time.sleep(a)
    print("Path 1: This path winds through the east side of the frozen wasteland.")
    time.sleep(a)
    print("Path 2: This path leads through a nearby town inhabited by locals.")
    time.sleep(a)
    print("Path 3: This path will lead to the forest.")
    time.sleep(a)
    pathone = input("Which path will you choose? (1/2/3/)")
    if pathone == '1':
        print()
        path1()
    elif pathone == '2':
        print()
        path2()




def death1():
    print("You are being shot, and you try to fight back.")
    time.sleep(a)
    print("You run and hide in cover. You have one bandage and you bandage yourself.")




def path2():
    print()
    print("You go on a short walk to the town nearby.")
    time.sleep(a)
    print("You enter the town, but you spot a German Patrol.")
    time.sleep(a)
    print("You contemplate to engage them, but there are many of them. What will you do?")
    time.sleep(a)
    print("Press 1 to engage, press 2 to hide in the bushes.")
    respon2 = input("Enter your response now.")
     if respon2 == '1':
     print()
     death1()


def path1():
    print()
    print("You begin to travel through miles of barren wasteland.")
    time.sleep(a)
    print("Suddenly, you see a vehicle driving towards you, it appears to be a Jeep.")
    time.sleep(a)
    print("The Jeep stops, a figure steps out of the Jeep.")
    time.sleep(a)
    print()
    t1 = '"I am Lieutenant Heinz Bormann of the SS, I see that you are traveling alone. Can I help you?"'
    print()
    for character in t1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    path1_1()


def path1_1():
    resp1 = input("Will you let Heinz help you? (Y/N)")
    if resp1 == 'n' or resp1 == 'N':
        t3 = '"Very well then, be on your way."'
        print()
        for character in t3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
        time.sleep(a)
        print("Your journey through the wasteland continues.")
        time.sleep(a)
        print("You travel, and travel, but there is no one or nothing in sight for miles.")
        time.sleep(a)
        water1 = input("You have become thirsty, press 1 to find some water.")
        if water1 == '1':
            print('You take a drink of water from a freshwater lake.')
        else:
            print('I dont know what to say, please follow the commands given.')
        time.sleep(a)
        print('You begin to see smoke from the battlefield.')
        time.sleep(a)
        print('The sounds of booming artillery becomes more deafening as you reach the battlefield.')
        time.sleep(a)
        print('You have reached friendly trenches, a fellow soldier leads you to the Commander.')
        t4 = '"Well done, soldier. You have served your country well. Thanks to these plans, we will stop the German ' \
             'offense." '
        print()
        for character in t4:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
    elif resp1 == 'y' or resp1 == 'Y':
        print('You let Heinz see the piece of paper in your Pocket.')
        time.sleep(a)
        print('He discovers that these are plans plotting against his army.')
        time.sleep(a)
        t2 = '"Ah, I see that you are a traitor of the Reich. In the name of a greater Germany you will die."'
        print()
        for character in t2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
        print('Your story for a free Norway ends here, as the SS Lieutenant has shot you.')
    else:
        print("I don't know what to say, please follow the commands given.")


startGame = input("Would you like to embark on this Journey? (Y/N)")
if startGame == 'n' or startGame == 'N':
    print('Maybe we will see you again in the near future.')
elif startGame == 'y' or startGame == 'Y':
    name = input("Please enter your name.")
    print(name + ' Private First Class, Your Journey Begins.')
    introduction()
else:
    print('I dont know what to say, please follow the commands given.')
