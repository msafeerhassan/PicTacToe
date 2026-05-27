import os
import random

mainArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
user1wins = 0
user2wins = 0
user1Name = str(input("User 1 Name: "))
user2Name = str(input("User 2 Name: "))


def createBoard():
    for i in range(9):
        if i % 3 == 0 and i!=0:
            print("\n")
        print(mainArr[i], " ", end="")

def user1Turn():
    while True:
        position = int(input(f"\n\n{user1Name}'s Turn (X): "))
        arrPosition = position - 1
        if position < 1 or position > 9 or mainArr[arrPosition] == "X" or mainArr[arrPosition] == "O":
            print("Choose another option")
        else: 
            mainArr[arrPosition] = "X"
            break

def user2Turn():
    while True:
        position = int(input(f"\n\n{user2Name}'s Turn (O): "))
        arrPosition = position - 1
        if position < 1 or position > 9 or mainArr[arrPosition] == "X" or mainArr[arrPosition] == "O":
            print("Choose another option")
            pass
        else: 
            mainArr[arrPosition] = "O"
            break

def computerTurn():
    while True:
        position = random.randrange(1,9,1)
        arrPosition = position - 1
        if mainArr[arrPosition] == "X" or mainArr[arrPosition] == "O":
            pass
        else:
            mainArr[arrPosition] = "O"
            break

def checkWin(arr):
    global user1wins, user2wins
    if arr[0] == arr[1] and arr[1] == arr[2]:
        if arr[0] == "X":
            print(f"{user1Name} won!")
            user1wins += 1
        else:
            print(f"{user2Name} won!")
            user2wins += 1
        return True
    elif arr[3] == arr[4] and arr[4] == arr[5]:
        if arr[3] == "X":
            print(f"{user1Name} won!")
            user1wins += 1
        else:
            print(f"{user2Name} won!")
            user2wins += 1
        return True
    elif arr[6] == arr[7] and arr[7] == arr[8]:
        if arr[6] == "X":
            print(f"{user1Name} won!")
            user1wins += 1
        else:
            print(f"{user2Name} won!")
            user2wins += 1
        return True
    elif arr[0] == arr[3] and arr[3] == arr[6]:
        if arr[0] == "X":
            print(f"{user1Name} won!")
            user1wins += 1
        else:
            print(f"{user2Name} won!")
            user2wins += 1
        return True
    elif arr[1] == arr[4] and arr[4] == arr[7]:
        if arr[1] == "X":
            print(f"{user1Name} won!")
            user1wins += 1
        else:
            print(f"{user2Name} won!")
            user2wins += 1
        return True
    elif arr[2] == arr[5] and arr[5] == arr[8]:
        if arr[2] == "X":
            print(f"{user1Name} won!")
            user1wins += 1
        else:
            print(f"{user2Name} won!")
            user2wins += 1
        return True
    elif arr[0] == arr[4] and arr[4] == arr[8]:
        if arr[0] == "X":
            print(f"{user1Name} won!")
            user1wins += 1
        else:
            print(f"{user2Name} won!")
            user2wins += 1
        return True
    elif arr[2] == arr[4] and arr[4] == arr[6]:
        if arr[2] == "X":
            print(f"{user1Name} won!")
            user1wins += 1
        else:
            print(f"{user2Name} won!")
            user2wins += 1
        return True
    elif arr[0] != '1' and arr[1] != '2' and arr[2] != '3' and arr[3] != '4' and arr[4] != '5' and arr[5] != '6' and arr[6] != '7' and arr[7] != '8' and arr[8] != '9':
        print("It's a draw :)")
        return True
    else:
        return False
    
def clearBoard():
    for i in range(9):
        value = i + 1
        mainArr[i] = str(value)
    print("Board reset complete!")

createBoard()
while True:

    user1Turn()
    os.system('cls')
    createBoard()
    print("\n")
    if checkWin(mainArr) == True:
        print(f"{user1Name}'s Wins: {user1wins}")
        print(f"{user2Name}'s Wins: {user2wins}")
        if user1wins > user2wins:
            print(f"{user1Name} is leading!!")
        elif user2wins > user1wins:
            print(f"{user2Name} is leading!!")
        else:
            print("Waiting for someone to claim lead :(")
        while True:
            consent = input("Would you like to play again? (y/n): ")
            if consent == "Y" or consent == "y":
                clearBoard()
                createBoard()
                break
            elif consent == "n" or consent == "N":
                exit()
            else:
                print("Please either choose Y or N!!")
                pass
    else:
        pass
    user2Turn()
    os.system('cls')
    createBoard()
    print("\n")
    if checkWin(mainArr) == True:
        print(f"User 1 Wins: {user1wins}")
        print(f"User 2 Wins: {user2wins}")
        if user1wins > user2wins:
            print(f"{user1Name} is leading!!")
        elif user2wins > user1wins:
            print(f"{user2Name} is leading!!")
        else:
            print("Waiting for someone to claim lead :(")
        while True:
            consent = input("Would you like to play again? (y/n): ")
            if consent == "Y" or consent == "y":
                clearBoard()
                createBoard()
                break
            elif consent == "n" or consent == "N":
                exit()
            else:
                print("Please either choose Y or N!!")
                pass
    else:
        pass