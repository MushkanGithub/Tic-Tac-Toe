# Tic Tac Toe (for both Single Player vs Computer and Double Players)
from tkinter import *
root=Tk()
root.geometry("330x550")
root.title("Tic Tac Toe")
root.resizable(0,0)
frame1=Frame(root)
frame1.pack()
titleLabel=Label(frame1,text="Tic tac toe", font=("Arial",26),bg="orange",width=16)
titleLabel.grid(row=0,column=0)

optionFrame= Frame(root,bg="grey")
optionFrame.pack()

frame2=Frame(root)
frame2.pack()

board={1:" ", 2:" ", 3:" ",
       4:" ", 5:" ", 6:" ",
       7:" ", 8:" ", 9:" "}

turn="x"
game_end=False
mode="singlePlayer"

def changeModeToSingleplayer():
    global mode
    mode= "singlePlayer"
    spButton["bg"]="lightgreen"
    mpButton["bg"] = "lightgrey"

def changeModeToMultiplayer():
    global mode
    mode= "multiPlayer"
    mpButton["bg"] = "lightgreen"
    spButton["bg"] = "lightgrey"

def updateBoard():
    for i in board.keys():
        button[i-1]["text"]=board[i]
    #rows
    if((button[0]["text"] == button[1]["text"]) and button[1]["text"] == button[2]["text"] and button[2][
        "text"] == 'o'):
        button[0]["bg"]="green"
        button[1]["bg"] = "green"
        button[2]["bg"] = "green"
    elif((button[0]["text"] == button[1]["text"]) and button[1]["text"] == button[2]["text"] and button[2][
        "text"] == 'x'):
        button[0]["bg"] = "green"
        button[1]["bg"] = "green"
        button[2]["bg"] = "green"
    elif((button[3]["text"] == button[4]["text"]) and button[4]["text"] == button[5]["text"] and button[5][
        "text"] == 'o'):
        button[3]["bg"] = "green"
        button[4]["bg"] = "green"
        button[5]["bg"] = "green"
    elif((button[3]["text"] == button[4]["text"]) and button[4]["text"] == button[5]["text"] and button[5][
        "text"] == 'x'):
        button[3]["bg"] = "green"
        button[4]["bg"] = "green"
        button[5]["bg"] = "green"
    elif ((button[6]["text"] == button[7]["text"]) and button[7]["text"] == button[8]["text"] and button[8][
        "text"] == 'x'):
        button[6]["bg"] = "green"
        button[7]["bg"] = "green"
        button[8]["bg"] = "green"
    elif((button[6]["text"] == button[7]["text"]) and button[7]["text"] == button[8]["text"] and button[8][
        "text"] == 'o'):
        button[6]["bg"] = "green"
        button[7]["bg"] = "green"
        button[8]["bg"] = "green"
    #columns
    elif((button[0]["text"] == button[3]["text"]) and button[3]["text"] == button[6]["text"] and button[6][
        "text"] == 'x'):
        button[0]["bg"] = "green"
        button[3]["bg"] = "green"
        button[6]["bg"] = "green"
    elif((button[0]["text"] == button[3]["text"]) and button[3]["text"] == button[6]["text"] and button[6][
        "text"] == 'o'):
        button[0]["bg"] = "green"
        button[3]["bg"] = "green"
        button[6]["bg"] = "green"
    elif((button[1]["text"] == button[4]["text"]) and button[4]["text"] == button[7]["text"] and button[7][
        "text"] == 'x'):
        button[1]["bg"] = "green"
        button[4]["bg"] = "green"
        button[7]["bg"] = "green"
    elif((button[1]["text"] == button[4]["text"]) and button[4]["text"] == button[7]["text"] and button[7][
        "text"] == 'o'):
        button[1]["bg"] = "green"
        button[4]["bg"] = "green"
        button[7]["bg"] = "green"
    elif((button[2]["text"] == button[5]["text"]) and button[5]["text"] == button[8]["text"] and button[8][
        "text"] == 'x'):
        button[2]["bg"] = "green"
        button[5]["bg"] = "green"
        button[8]["bg"] = "green"
    elif((button[2]["text"] == button[5]["text"]) and button[5]["text"] == button[8]["text"] and button[8][
        "text"] == 'o'):
        button[2]["bg"] = "green"
        button[5]["bg"] = "green"
        button[8]["bg"] = "green"
    #diagonals
    elif((button[0]["text"] == button[4]["text"]) and button[4]["text"] == button[8]["text"] and button[8][
        "text"] == 'x'):
        button[0]["bg"] = "green"
        button[4]["bg"] = "green"
        button[8]["bg"] = "green"
    elif((button[0]["text"] == button[4]["text"]) and button[4]["text"] == button[8]["text"] and button[8][
        "text"] == 'o'):
        button[0]["bg"] = "green"
        button[4]["bg"] = "green"
        button[8]["bg"] = "green"
    elif((button[2]["text"] == button[4]["text"]) and button[4]["text"] == button[6]["text"] and button[6][
        "text"] == 'x'):
        button[2]["bg"] = "green"
        button[4]["bg"] = "green"
        button[6]["bg"] = "green"
    elif((button[2]["text"] == button[4]["text"]) and button[4]["text"] == button[6]["text"] and button[6][
        "text"] == 'o'):
        button[2]["bg"] = "green"
        button[4]["bg"] = "green"
        button[6]["bg"] = "green"

def checkForWin(player):
    # for rows
    if(board[1]==board[2] and board[2]==board[3] and board[3]==player):
        return True
    elif(board[4]==board[5] and board[5]==board[6] and board[6]==player):
        return True
    elif(board[7]==board[8] and board[8]==board[9] and board[9]==player):
        return True
    # for columns
    if (board[1] == board[4] and board[4] == board[7] and board[7] == player):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[8] == player):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[9] == player):
        return True
    # for diagonals
    if (board[1] == board[5] and board[5] == board[9] and board[9] == player):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[7] == player):
        return True

def checkForDraw():
    for i in board.keys():
        if(board[i]==" "):
            return False
    return True

def restartGame():
    global game_end
    game_end=False
    for i in button:
        i["text"]=" "
        i["bg"]="yellow"
    for i in board.keys():
        board[i]=" "
    titleLabel = Label(frame1, text="Tic tac toe", font=("Arial", 26), bg="orange",width=16)
    titleLabel.grid(row=0, column=0)

def minimax(board,isMaximizing):  #isMaximizing tells whether computer is currently playing the game or not
    if(checkForWin('o')):
        return 1
    if(checkForWin('x')):
        return -1
    if(checkForDraw()):
        return 0
    if(isMaximizing):
        bestScore = -100
        for i in board.keys():
            if board[i] == " ":
                board[i] = "o"
                score = minimax(board, False)  # minimax
                board[i] = " "
                if (score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 100
        for i in board.keys():
            if board[i] == " ":
                board[i] = "x"
                score = minimax(board, True)  # minimax
                board[i] = " "
                if (score < bestScore):
                    bestScore = score
        return bestScore

def playComputer():
    bestScore=-100
    bestMove=9    #[1-9]
    for i in board.keys():
        if board[i]==" ":
            board[i]="o"
            score=minimax(board,False) #minimax
            board[i]=" "
            if(score>bestScore):
                bestScore=score
                bestMove=i
    board[bestMove]="o"

def play(event):
    global turn,game_end
    if (game_end):
        return
    key=event.widget
    key2=str(key)
    clicked=key2[-1]
    if(clicked=="n"):
        clicked=1
    else:
        clicked=int(clicked)
    if(key["text"]==" "):
        if(turn=="x"):
            board[clicked]=turn
            if (checkForWin(turn)):
                winningLabel = Label(frame1, text=f"{turn} wins the game",bg="grey",font=("Arial",26),width=16)
                winningLabel.grid(row=0, column=0, columnspan=3)
                game_end=True
            turn="o"
            updateBoard()
            if(mode=="singlePlayer"):
                playComputer()
                if (checkForWin(turn)):
                    winningLabel = Label(frame1, text=f"{turn} wins the game",bg="grey",font=("Arial",26),width=16)
                    winningLabel.grid(row=0, column=0, columnspan=3)
                    game_end=True
                turn="x"
                updateBoard()
        else:
            board[clicked]=turn
            updateBoard()
            if (checkForWin(turn)):
                winningLabel=Label(frame1,text=f"{turn} wins the game",bg="grey",font=("Arial",26),width=16)
                winningLabel.grid(row=0,column=0,columnspan=3)
                game_end=True
            turn="x"
        if(checkForDraw()):
            drawLabel=Label(frame1,text="Game Draw",bg="grey",font=("Arial",26),width=16)
            drawLabel.grid(row=0, column=0, columnspan=3)
        print(board) #to know the status of board

#change mode options (multiplayer,singleplayer)
spButton=Button(optionFrame,text="Single Player",width=13,height=1,
                     font=("Arial",15),bg="lightgrey",relief=RAISED,borderwidth=5,command=changeModeToSingleplayer)
spButton.grid(row=0,column=0,columnspan=1,sticky=NW)
mpButton=Button(optionFrame,text="Multi Player",width=13,height=1,
                     font=("Arial",15),bg="lightgrey",relief=RAISED,borderwidth=5,command=changeModeToMultiplayer)
mpButton.grid(row=0,column=1,columnspan=1,sticky=NW)

rowvalue=0
columnvalue=0
button=[1,2,3,4,5,6,7,8,9]
for i in range(9):
    button[i]=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="yellow",relief=RAISED,borderwidth=5,activebackground="brown")
    button[i].grid(row=rowvalue,column=columnvalue)
    button[i].bind("<Button-1>",play)
    columnvalue+=1
    if(columnvalue>2):
        rowvalue+=1
        columnvalue=0

restartButton=Button(frame2,text="Restart Game",width=19,height=1,
                     font=("Arial",20),bg="Green",relief=RAISED,borderwidth=5,command=restartGame)
restartButton.grid(row=4,column=0,columnspan=3)
root.mainloop()