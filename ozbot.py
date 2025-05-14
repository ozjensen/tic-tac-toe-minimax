import os
import random
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def display_board(board):
    clear_screen()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])
def player_input():
    marker = ''
    #ask player 1 to choose X or O
    while marker != 'X' and marker!= 'O':
        marker = input('Player1, choose X or O: ').strip().upper()
    # assign player 2, the opposite marker
    player1 = marker
    if player1 =='X':
        player2 = 'O'
    else:
        player2 = 'X'
    print(f"Player 1 is {player1}!  Player 2 is {player2}!")
    return(player1,player2)
def place_marker(board, marker, position):
        board[position] = marker
def clear_board(board):
    for i in range(1, 10):
        board[i] = ' '
wins = [
    (1, 2, 3),  # rows
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),  # columns
    (2, 5, 8),
    (3, 6, 9), 
    (1, 5, 9),  # diagonals
    (3, 5, 7)
]       
def win_check (board,mark):
    for  (i, j, k) in wins:
        if board [i] == board [j] == board [k]  ==mark:
            return True
    else:
        return False
def full_board_check(board):
    return all(space !=' ' for space in board[1:])
import random
def choose_first():
    choice = random.choice(['Player 1','Player 2'])
    print (f'{choice} goes first!')
    return choice
def space_check(board, position):
    return board[position] == ' '
def gameover_check(board, player, markers):
    #win?
    if win_check(board,markers):
        print(f"{player} wins!")
        return True
    #tie?
    if full_board_check(board):
        print ("It is a tie, you both LOSE!")
        return True
    else: 
        return False
def player_choice(board):
    position = 0
    while True: 
        choice = input("Choose your next position (1-9): ").strip()
                #check if it's a digit
        if not choice.isdigit():
            print("That's not a number, silly. Try Again!")
            continue
        position =int(choice)
        # Check if it is in range
        if position not in range(1,10):
            print("Out of range! Please choose a number between 1 and 9.")
            continue
        if not space_check(board, position):
            print ("That space is already taken. Pick another.")
            continue
            # ALL GOOD
        return position
def replay():
    choice = ''
    while choice not in ('Y','N'):
        choice = input("Play again? Enter Y or N: ").strip().upper()
    return choice =='Y'
def computer_choice(board,comp_mark,player_mark):
    best_score = -float('inf')
    best_move = None
    #1) Loop over positions 1-9
    for i in range(1,10):
        if space_check(board, i):
    #2) board[i] = comp_mark
            board[i] = comp_mark
    #3) call minimax to evaluate this move
            score = minimax(board, 0, False, comp_mark, player_mark)
    #4) undo the move
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
def minimax(board, depth, is_maximizing, comp_mark, player_mark):
    #check for (Win/Loss/Tie)
    if win_check(board, comp_mark):
        return 10 - depth
    if win_check(board,player_mark): 
        return depth - 10
    if full_board_check(board):
        return 0
    #2) maximizing turn (computer)
    if is_maximizing:
        best_score = -float('inf')
        for i in range(1,10):
            if space_check(board, i):
                board[i] = comp_mark
                score = minimax(board, depth+1, False, comp_mark, player_mark)
                board[i] = ' '
                best_score = max(best_score,score)
        return best_score
        #3) minimizing turn (human)
    else: 
        best_score = float('inf')
        for i in range(1, 10):
            if space_check(board,i):
                board[i] = player_mark
                score = minimax(board, depth+1, True, comp_mark, player_mark)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score
def ozbot():
    print("Welcome to Oz's Tic Tac Toe!")
    while True:
        clear_board(test_board)

    
        player1_marker, player2_marker = player_input()

        
        current_player = choose_first()
        current_marker = (player1_marker if current_player == "Player 1"
                                         else player2_marker)
            
        print(f"{current_player} will go first, playing as '{current_marker}'.")
        input("Press Enter to start the game")
        game_on = True
        while game_on:
            display_board(test_board)
            print (f"{current_player}'s turn! ({current_marker})")
    

            if current_player == "Player 1":
                pos = player_choice(test_board)
            else:
                pos = computer_choice(test_board,current_marker,player1_marker)
            place_marker (test_board, current_marker, pos)
            display_board(test_board)
            if gameover_check(test_board, current_player, current_marker):
                game_on = False
            else:

           
                if current_player == "Player 1":
                    current_player = "Player 2"
                    current_marker = player2_marker
                else: 
                    current_player = "Player 1" 
                    current_marker = player1_marker        

        if not replay():
            print("Thanks for playing Oz's Tic Tac Toe!")
            break
if __name__ == "__main__":
    ozbot()








