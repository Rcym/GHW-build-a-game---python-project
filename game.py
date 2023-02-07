# tkinter is a GUI library
import tkinter as tk
import math


window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("400x500")
window.resizable(False, False)
window.configure(bg="#333")

title = tk.Label(window, text="Tic Tac Toe", font=("Arial", 20), bg="#333", fg="#fff", pady=5)
title.pack()

conainer = tk.Frame(window, bg="#333", width=300, height=300, padx=50, pady=50)
conainer.pack()

# creating a button for each 3x3 cell
button11 = tk.Button(conainer, text="", font=("Arial", 20), bg="#fff", fg="#333", width=5, height=2, command=lambda: buttonClicked(button11))
button12 = tk.Button(conainer, text="", font=("Arial", 20), bg="#fff", fg="#333", width=5, height=2, command=lambda: buttonClicked(button12))
button13 = tk.Button(conainer, text="", font=("Arial", 20), bg="#fff", fg="#333", width=5, height=2, command=lambda: buttonClicked(button13))

button21 = tk.Button(conainer, text="", font=("Arial", 20), bg="#fff", fg="#333", width=5, height=2, command=lambda: buttonClicked(button21))
button22 = tk.Button(conainer, text="", font=("Arial", 20), bg="#fff", fg="#333", width=5, height=2, command=lambda: buttonClicked(button22))
button23 = tk.Button(conainer, text="", font=("Arial", 20), bg="#fff", fg="#333", width=5, height=2, command=lambda: buttonClicked(button23))

button31 = tk.Button(conainer, text="", font=("Arial", 20), bg="#fff", fg="#333", width=5, height=2, command=lambda: buttonClicked(button31))
button32 = tk.Button(conainer, text="", font=("Arial", 20), bg="#fff", fg="#333", width=5, height=2, command=lambda: buttonClicked(button32))
button33 = tk.Button(conainer, text="", font=("Arial", 20), bg="#fff", fg="#333", width=5, height=2, command=lambda: buttonClicked(button33))

# placing the buttons on the grid
button11.grid(row=0, column=0)
button12.grid(row=0, column=1)
button13.grid(row=0, column=2)

button21.grid(row=1, column=0)
button22.grid(row=1, column=1)
button23.grid(row=1, column=2)

button31.grid(row=2, column=0)
button32.grid(row=2, column=1)
button33.grid(row=2, column=2)

retryBtn = tk.Button(window, text="Retry", font=("Arial", 20), bg="#fff", fg="#333", width=7, height=1, command=lambda: retryFunction())
retryBtn.pack()




def checkWin():
    # checking for horizontal wins
    if button11["text"] == button12["text"] == button13["text"] and button11["text"] == "X":
        return True
    elif button21["text"] == button22["text"] == button23["text"] and button21["text"] == "X":
        return True
    elif button31["text"] == button32["text"] == button33["text"] and button31["text"] == "X":
        return True
    # checking for vertical wins
    elif button11["text"] == button21["text"] == button31["text"] and button11["text"] == "X":
        return True
    elif button12["text"] == button22["text"] == button32["text"] and button12["text"] == "X":
        return True
    elif button13["text"] == button23["text"] == button33["text"] and button13["text"] == "X":
        return True
    # checking for diagonal wins
    elif button11["text"] == button22["text"] == button33["text"] and button11["text"] == "X":
        return True
    elif button13["text"] == button22["text"] == button31["text"] and button13["text"] == "X":
        return True
    else:
        return False

def checkLost():
    # checking for horizontal lost
    if button11["text"] == button12["text"] == button13["text"] and button11["text"] == "O":
        return True
    elif button21["text"] == button22["text"] == button23["text"] and button21["text"] == "O":
        return True
    elif button31["text"] == button32["text"] == button33["text"] and button31["text"] == "O":
        return True
    # checking for vertical lost
    elif button11["text"] == button21["text"] == button31["text"] and button11["text"] == "O":
        return True
    elif button12["text"] == button22["text"] == button32["text"] and button12["text"] == "O":
        return True
    elif button13["text"] == button23["text"] == button33["text"] and button13["text"] == "O":
        return True
    # checking for diagonal lost
    elif button11["text"] == button22["text"] == button33["text"] and button11["text"] == "O":
        return True
    elif button13["text"] == button22["text"] == button31["text"] and button13["text"] == "O":
        return True
    else:
        return False
    
allBtns = [button11, button12, button13, button21, button22, button23, button31, button32, button33]
availableBtns = [button11, button12, button13, button21, button22, button23, button31, button32, button33]
xPlaced = 0

def buttonClicked(clickedBtn) :
    global xPlaced
    xPlaced += 2

    if xPlaced == 8:
        print("Draw!")
        for btn in allBtns:
            btn["bg"] = "#ff0"

    if clickedBtn["text"] == "":
        clickedBtn["text"] = "X"
        clickedBtn["state"] = "disabled"
        availableBtns.remove(clickedBtn)

    if checkWin():
        print("You win!")
        for btn in allBtns:
            btn["bg"] = "#0f0"
    

    # AI's turn
    # AI will always pick the middle cell if it's available
    if button22["text"] == "":
        button22["text"] = "O"
        button22["state"] = "disabled"
        availableBtns.remove(button22)
    else:
        # AI will pick a random cell
        import random
        randomBtn = random.choice(availableBtns)
        availableBtns.remove(randomBtn)
        randomBtn["text"] = "O"
        randomBtn["state"] = "disabled"
        
    if checkLost():
        print("You lost!")
        for btn in allBtns:
            btn["bg"] = "#f00"

    
def retryFunction():
    global availableBtns
    global xPlaced

    for btn in allBtns:
        btn["text"] = ""
        btn["state"] = "normal"
        btn["bg"] = "#fff"
        xPlaced = 0
        availableBtns = [button11, button12, button13, button21, button22, button23, button31, button32, button33]



window.mainloop()