from tkinter import *
root = Tk()
from tkinter.font import Font

import random

root.geometry("500x800")  # 5 words width 6 words height 2 words keyboard height
root.title("wordle")
root.iconbitmap("./resources/ico.ico")


class Board:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self):
        self.tiles = []
        self.answer = ""
        self.word = []
        self.correctness = [0, 0, 0, 0, 0]
        self.pointer = 0
        self.row = 0
        self.frame = Frame(root)
        self.frame.place(x=55, y=50)
        self.new = Button(root, text="NEW", command=lambda:self.newGame())
        self.new.place(x=250, y=20)
        self.font = Font(family="Helvetica", size="15", weight="bold")

        root.bind("<Key>", self.keyPressed)

        self.createBoard()

    def createBoard(self):
        counter = 0
        for y in range(6):
            for x in range(5):
                label = Label(self.frame, bd=3, bg="ivory", padx=34, pady=28, font=self.font)
                tile = Tile(_id=counter, pos=[x, y], label=label)
                self.tiles.append(tile)
                counter += 1

    def newGame(self):
        self.answer = self.getRandomWord()
        print(self.answer)
        self.correctness = [0, 0, 0, 0, 0]
        self.row = 0
        self.pointer = 0
        self.word = []
        for x in self.tiles:
            x.label.config(text="")
            x.label.config(bg="ivory")

    def getRandomWord(self):
        with open("./resources/answers.txt") as file:
            choice = random.choice(file.readlines()).strip("\n")
        return choice

    def getAllWords(self):
        with open("./resources/guesses(2).txt") as file:
            lines = file.read().split("\n")
        return lines

    def keyPressed(self, event):
        key = event.keysym

        if key in board.ALPHABET:
            if self.pointer < 5:
                tile = self.tiles[self.pointer+(5*self.row)]
                tile.label.config(text=key)
                self.word.append(key)
                self.pointer += 1

        elif key == "BackSpace":
            if self.pointer > 0:
                self.pointer -= 1
                tile = self.tiles[self.pointer+(5*self.row)]
                tile.label.config(text="")
                self.word.pop(-1)

        elif key == "Return":

            if len(self.word) == 5:  # word is 5 characters long

                allWords = self.getAllWords()

                if "".join(self.word) in allWords:  # word is in word list

                    for x in range(len(self.word)):  # iteration through every letter in the word

                        if self.word[x] == self.answer[x]:
                            self.correctness[x] = 2  # green
                            self.tiles[x+(5*self.row)].label.config(bg="green")

                        elif self.word[x] in self.answer:
                            self.correctness[x] = 1  # yellow
                            self.tiles[x+(5*self.row)].label.config(bg="yellow")

                        else:
                            self.correctness[x] = 0  # grey
                            self.tiles[x + (5 * self.row)].label.config(bg="grey")

                    if not ((0 in self.correctness) or (1 in self.correctness)):

                        print(self.correctness, "you win")
                        return

                    self.row += 1
                    self.word = []
                    self.pointer = 0
                    self.correctness = [0, 0, 0, 0, 0]

                else:
                    print("not in word list")


class Tile:
    def __init__(self, _id, pos, label):
        self.id = _id
        self.pos = pos
        self.label = label
        self.label.grid(row=pos[1], column=pos[0])

board = Board()
board.newGame()

root.mainloop()