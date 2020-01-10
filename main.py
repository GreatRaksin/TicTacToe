from tkinter import *
import random

root = Tk()
root.title('Tic Tac Toe')
run = True
field = []
counter = 0


def start():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global run
    run = True
    global counter
    counter = 0


def userMove(row, col):
    if run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global counter
        counter += 1
        checkWin('X')
        if run and counter < 5:
            aiMove()
            checkWin('O')


def checkWin(smb):
    for n in range(3):
        checkLine(field[n][0], field[n][1], field[n][2], smb)
        checkLine(field[0][n], field[1][n], field[2][n], smb)
    checkLine(field[0][0], field[1][1], field[2][2], smb)
    checkLine(field[2][0], field[1][1], field[0][2], smb)


def checkLine(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global run
        run = False


def isWin(a1, a2, a3, smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res


def aiMove():
    for n in range(3):
        if isWin(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if isWin(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if isWin(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if isWin(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if isWin(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if isWin(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if isWin(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if isWin(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break


for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 24, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: userMove(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
newBtn = Button(root, text='new game', command=start)
newBtn.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()
