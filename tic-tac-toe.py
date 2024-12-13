import random

print("Welcome to Game of Tic-Tac-Toe")
print("By Emir Kerem Işıldar")

def isValid(movement, moves, backTable, table, playerTurn):
    if movement == "00":  
        return False, playerTurn
    elif movement in moves: 
        print("That cell is already full. Try Again.")
        return True, playerTurn
    elif (movement[0] in "123") and (movement[1] in "abc"):  
        row = int(movement[0]) - 1
        col = "abc".index(movement[1])
        if backTable[row][col] == 0:  
            backTable[row][col] = 1
            
            temp = list(table[2 * row + 2])  
            position = 7 + col * 6  
            temp[position] = "X"
            table[2 * row + 2] = "".join(temp)
            
            moves.append(movement)
            return True, 2  
        else:
            print("That cell is already full. Try Again.")
            return True, playerTurn
    else:  
        print("Invalid input. Try Again.")
        return True, playerTurn




def printTable(table):
    for line in table:
        print(line)



'''
for check()

#side by side
[0][0] | [0][1] | [0][2]
[1][0] | [1][1] | [1][2]
[2][0] | [2][1] | [2][2]

#bottom to top
[0][0] | [1][0] | [2][0]
[0][1] | [1][1] | [2][1]
[0][2] | [1][2] | [2][2]

#cross
[0][0] | [1][1] | [2][2]
[2][0] | [1][1] | [0][2]
'''

def check(backTable):
    
    for row in range(3):
        if backTable[row][0] == backTable[row][1] == backTable[row][2] and backTable[row][0] != 0:
            if backTable[row][0] == 2:
                return "Game Over. I Win!"
            else:
                return "Congratulations. You Win!"

   
    for col in range(3):
        if backTable[0][col] == backTable[1][col] == backTable[2][col] and backTable[0][col] != 0:
            if backTable[0][col] == 2:
                return "Game Over. I Win!"
            else:
                return "Congratulations. You Win!"

    
    if backTable[0][0] == backTable[1][1] == backTable[2][2] and backTable[0][0] != 0:
        if backTable[0][0] == 2:
            return "Game Over. I Win!"
        else:
            return "Congratulations. You Win!"
    if backTable[2][0] == backTable[1][1] == backTable[0][2] and backTable[2][0] != 0:
        if backTable[2][0] == 2:
            return "Game Over. I Win!"
        else:
            return "Congratulations. You Win!"

    
    if all(backTable[row][col] != 0 for row in range(3) for col in range(3)):
        return "It is a tie!"

    
    return None


table = [
    "    |  a  |  b  |  c  |",  # 0 * 
    "----+-----+-----+-----|",  # 1 - 
    " 1  |     |     |     |",  # 2 + 
    "----+-----+-----+-----|",  # 3 -
    " 2  |     |     |     |",  # 4 +
    "----+-----+-----+-----|",  # 5 -
    " 3  |     |     |     |",  # 6 +
    "----+-----+-----+-----|"   # 7 -
]

printTable(table)

playerTurn = random.randint(1, 2)  
backTable = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
moves = []

while True:
    if playerTurn == 2:  
        print("Computer's turn!")
        while True:  
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            move = str(row + 1) + chr(col + ord('a'))

            if move not in moves and backTable[row][col] == 0:
                backTable[row][col] = 2 
                temp = list(table[2 * row + 2])  
                position = 7 + col * 6  
                temp[position] = "O"
                table[2 * row + 2] = "".join(temp)  
 
                moves.append(move)
                break

        printTable(table)
        
        result = check(backTable)
        if result:
            print(result)
            break
        
        playerTurn = 1  
    else:  
        
        move = input("Your Move (Enter 00 to Exit)? ")
        is_valid, playerTurn = isValid(move, moves, backTable, table, playerTurn)  
        if not is_valid:  
            print("Thank You for Playing Tic-Tac-Toe")
            break
        printTable(table)
        
        result = check(backTable)
        if result:
            print(result)
            break

        
         