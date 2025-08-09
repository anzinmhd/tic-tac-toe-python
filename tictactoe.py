import tkinter  #tk interface (graphical interface)

def set_tile(row,col):
       global curr_player
       if(game_over):
              return
       if(board[row][col]["text"]!=""):
              return #avoid the rewriting on already taken board
       board[row][col]["text"]=curr_player # mark the board
       if(curr_player==playerX): #switch player
              curr_player=playerO
       else:
              curr_player=playerX
       label["text"]=curr_player+"'s turn"
       check_winner()




def check_winner():
       global turns,game_over
       turns+=1
       #check horizontally
       for row in range(3):
              if (board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"] and board[row][0]["text"]!=""):
                     label.config(text=board[row][0]["text"]+" is the winner!",foreground=color_yellow)
                     for col in range(3):
                            board[row][col].config(foreground=color_yellow,background=color_light_gray)
                     game_over=True
                     return
       #check vertically
       for col in range(3):
              if(board[0][col]["text"]==board[1][col]["text"]==board[2][col]["text"] and board[0][col]["text"]!=""):
                     label.config(text=board[0][col]["text"]+" is the winner!",foreground=color_yellow,background=color_light_gray)
                     for row in range(3):
                            board[row][col].config(background=color_light_gray,foreground=color_yellow)
                     game_over=True
                     return
       #check diagonally
       if(board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"] and board[0][0]["text"]!=""):
              label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow,
                           background=color_light_gray)
              for i in range(3):
                     board[i][i].config(background=color_light_gray, foreground=color_yellow)
              game_over=True
              return
       #anti diagonally
       if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
              label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_yellow,
                           background=color_light_gray)
              board[0][2].config(background=color_light_gray, foreground=color_yellow)
              board[1][1].config(background=color_light_gray, foreground=color_yellow)
              board[2][0].config(background=color_light_gray, foreground=color_yellow)
              game_over=True
              return
       if(turns==9):
              label.config(text="Tie!", foreground=color_yellow,
                           background=color_light_gray)
              game_over=True
              return

def new_game():
       global turns,game_over
       turns=0
       game_over=False
       label.config(text=curr_player+"'s turn",foreground="white")
       for row in range(3):
              for col in range(3):
                     board[row][col].config(text="",foreground=color_blue,background=color_gray)

#game setup
turns=0
game_over=False
playerX="X"
playerO= "O"
curr_player=playerX
board=[[0,0,0],
       [0,0,0],
       [0,0,0]]
color_blue="#4584b6"
color_yellow="#ffff00"
color_gray="#343434"
color_light_gray="#646464"

#window
window=tkinter.Tk() #create game window
window.title("Tic Tac Toe")
window.resizable(False,False)
frame = tkinter.Frame(window)
label=tkinter.Label(frame,text=curr_player+"'s turn",font=("consolas",20),background=color_gray,foreground="white")
label.grid(row=0,column=0,columnspan=3,sticky="we") #To organize the label
for row in range(3):
       for col in  range(3):
              board[row][col]=tkinter.Button(frame,text="",font=("consolas",50,"bold"),background=color_gray,
                            foreground=color_blue,width=4,height=1,command=lambda row=row,column=col:set_tile(row,column)) #command lambda is to add action for clickin a button
              board[row][col].grid(row=row+1,column=col)
button=tkinter.Button(frame,text="Restart",font=("consolas",20),background=color_gray,foreground="white",command=new_game)
button.grid(row=4,column=0,columnspan=3,sticky="we")
frame.pack() #organize the frame

#center the window
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))

#format ((w)x(h)) +((x)+(y))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()

#over