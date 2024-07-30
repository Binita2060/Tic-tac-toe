def sum(a, b, c):
    return a + b + c

def printGameBoard(xState, yState):
    zero = 'X' if xState[0] else ('0' if yState[0] else 0)
    one = 'X' if xState[1] else ('0' if yState[1] else 1)
    two = 'X' if xState[2] else ('0' if yState[2] else 2)
    three = 'X' if xState[3] else ('0' if yState[3] else 3)
    four = 'X' if xState[4] else ('0' if yState[4] else 4)
    five = 'X' if xState[5] else ('0' if yState[5] else 5)
    six = 'X' if xState[6] else ('0' if yState[6] else 6)
    seven = 'X' if xState[7] else ('0' if yState[7] else 7)
    eight = 'X' if xState[8] else ('0' if yState[8] else 8)
    print(f" {zero}  |  {one}  |  {two}")#used to include expressions and variables directly within the string that is being printed.
    print(f"--- | --- | ---")
    print(f" {three}  |  {four}  |  {five}")
    print(f"--- | --- | ---")
    print(f" {six}  |  {seven}  |  {eight}")
     
def checkWinner(xState, yState):
    player_wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],[2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in player_wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("Congratulations..! Player X win the match.")
            return 1
        if (sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3):
            print("Congratulations..! Player Y win the match.")
            return 0
    return -1
        
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0 ,0, 0, 0]  #counting the position from zero as indexing in array
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 #1 for X-player and 0 for Y-Player
    print("\n \t \t \t \t \t \t  Welcome to Tic Tac Toe Game..!!")
    while(True):
        printGameBoard( xState, yState)
        if (turn == 1):
            print("It is a first player chance -- X's Chance.")
            value = int(input("Please enter the value: "))
            xState[value] = 1
        else:
            print("It is a second player chance -- Y's Chance")
            value = int(input("Please enter the value: "))
            yState[value] = 1
        
        cWin = checkWinner(xState, yState)
        if (cWin != -1):
            print("The match is over.")
            break
        
        turn = 1-turn
        
    if cWin == -1:
        print("The match ended in a draw.")