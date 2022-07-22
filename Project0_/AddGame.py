#!/usr/bin/env python3.5
# from playsound import playsound

import random
import os
import logging
logging.basicConfig()

def main():
    mathGame = ""
    mathGameLeaderboard = ""
    gameModeIsSetToTarget = False

    curriculum = "first grade to eighth grade math (optional: 9th grade math and above)"

    difficulty = random.randint(1, 8)

    ListOfOperators = ['+', '-', '<', '>', '<=', '>=']

    # if gameModeIsSetToTarget:
    #     # Ask User for a difficulty
    #     curriculum = userInput

    # while(True):
    #     equation = "read random subject from file curriculum and create an equation based on subject"
    #     userInput = "answer equation 'equation'"
    #     if userInput is right:
    #         score += 1
    #         # ADD EQUATION TO OUTPUT 
    #     else:
    #         # ADD EQUATION TO OUTPUT
        
    # print(score)
    print("Adding game press 'q' to quit")

    user_input = input("Do you want try to target mode? ")

    if user_input == "yes":
        gameModeIsSetToTarget = True
        
    if gameModeIsSetToTarget:
        targetscore = 0
        f = open('INPUTFILE.txt', 'r', encoding="utf-8")
        listoftargetequations = f.readlines()
        f.close()
    
        for equation in listoftargetequations:
            try:
                x = int(equation[:2])
                x_2 = int(equation[5:7])
            except:
                print("Error when parsing INPUT FILE")

            answer = x + x_2
            equation = str(x) + ' + ' + str(x_2) + ' = '
            user_input = input(equation)

            if user_input == str(answer):
                targetscore += 1
            elif user_input == 'q':
                break
        print(str(targetscore) + '/' + str(len(listoftargetequations)))

    listEquations = []
    isCorrect = []
    score = 0

    while(True):
        # os.system('clear')
        x = random.randint(0, 100)
        x_2 = random.randint(0, 100)

        answer = x + x_2
        equation = str(x) + ' + ' + str(x_2) + ' = '
        listEquations.append(equation + str(answer))
        user_input = input(equation)

        if user_input == str(answer):
            # playsound('/Users/Nilesh/Desktop/Correct (HD).mp3')
            isCorrect.append(True)
            score += 1
        elif user_input == 'q':
            isCorrect.append(False) 
            break
        else:
            isCorrect.append(False) 
    
    print(score)
    # WRITE EQUATIONS TO OUTPUT
    f = open('OUTPUTFILE.txt', 'w', encoding='utf-8')
    for equation in listEquations:
        f.write(equation)
        f.write('')
    f.close()

    user_input = input('Answers? Press "y": ')
    if(user_input == 'y'):
        count = 0
        while count < len(listEquations):
            print(listEquations[count] + ' ', end="")
            print(isCorrect[count])
            count += 1
    
if __name__ == "__main__":
    main()