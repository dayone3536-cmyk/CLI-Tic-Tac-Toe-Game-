#A simple CLI(command line interface) Tic Tac Toe which is organized into functions
print("welcome to my Tic Tac Toe")
try:
    def print_board(board):

        for i in range(0, 9, 3):
            print(board[i], "|", board[i+1], "|", board[i+2])

            if i < 6:
                print("---------")

    def check_winner(board):
        win_combo = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in win_combo:
            if board[a] == board[b] == board[c] != " ":
                print(f"{board[a]} WINS!!")
                return True

        if " " not  in board:
            print("its a tie")
            return True
        
        return False
        
    def swicth_players(current_player):

        current_player = "O" if current_player == "X" else "X"

        return current_player

    def get_move(current_player):
            while True:
                move = int(input(f"{current_player}'s Turn (1-9) 10 to quit"))
                move = move-1
                return move     
                   
    def check_move(move):
        if move == 9:
            print("Thanks for playing😊😊")
            return "quit"

        if move < 0 or move > 8:
            print("Invalid Try (1-9) 10 to quit")
            return "Invalid input"
    
    def reset():
        user_input = input("Do you want to play again??(y/n)").lower()
        if user_input in ["y","yes"]:
            return "reset"
        
        else:
            return "Over"

    def apply_move(move, current_player, board):
        if board[move] == " ":
            board[move] = current_player
            return "Not taken"
        else:
            print("Already Taken")
            return "Taken"
        
    def inner_game_loop():
        players = "X"
        board = [" "] * 9

        while True:
            print_board(board)
            move = get_move(players)

            # print(move)

            checking_move = check_move(move) #returning None
            # print(checking_move)

            if checking_move == "quit":
                return False
            
            elif checking_move == "Invalid input":
                continue

            applying_the_move = apply_move(move, players, board)
            # print(applying_the_move)

            if applying_the_move == "Taken": #Taken--placing over the placed marker
                continue

            players = swicth_players(players)

            winner = check_winner(board)
            if winner:
                reseting = reset()
                if reseting == "reset":
                    return True
                
                if reseting == "Over":
                    return False
                           
    def main_game():
        while True:
            game = inner_game_loop()
            if game:
                continue
            else:
                break
    main_game()

except ValueError:
    print("Invalid Closing...")