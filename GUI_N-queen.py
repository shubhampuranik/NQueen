from Tkinter import *
import math
import ttk
from nqueen2 import NQueen


def create(n, list1, number):
	frame = ttk.Frame(notebook)
	notebook.add(frame, text="Frame "+str(number+1))
	# print list1
	e = math.sqrt(250000 / (n * n))
	white = PhotoImage(file = "white.gif")
	black = PhotoImage(file = "black.gif")
	queen = PhotoImage(file = "q.gif")
	for i in range(0, n):
		for j in range(0, n):
			if (i + j) % 2 == 0:
				l1 = Label(frame, image = black, bg = "black", height = math.floor(e), width = math.floor(e))
				l1.photo = black
				l1.grid(row = i, column = j)
			else:
				l2 = Label(frame, image = white, bg = "black", height = math.floor(e), width = math.floor(e))
				l2.photo = white
				l2.grid(row = i, column = j)
	
	for i in range(0, n):
		d = (i + list1[i]) % 2
		if d == 0:
			l3 = Label(frame, image = queen, height = math.floor(e), width = math.floor(e), bg = "black")
			l3.photo = queen
			l3.grid(row = i, column = list1[i])
		else:
			l3 = Label(frame, image = queen, height = math.floor(e), width = math.floor(e), bg = "white")
			l3.photo = queen
			l3.grid(row = i, column = list1[i])


root = Tk()
notebook = ttk.Notebook(root)
root.state("normal")
n = input("enter value of n:")
nqueen2=NQueen(n)
output1 = nqueen2.get_result()
# if nqueen2.n > 10:
# 	exit()
for i in range(0, len(output1)):
	create(nqueen2.n, output1[i], i)
notebook.pack()
root.mainloop()
