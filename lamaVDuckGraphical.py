import Tkinter
from PIL import ImageTk, Image
import os
import time
import random
import numpy

width = 500
height = 500

tk = Tkinter.Tk()
tk.title('lama vs duck')
window = Tkinter.Canvas(tk, width = width, height = height)
tk.focus_set()
window.pack()


def parseInput(fileName):
	size = os.path.getsize(fileName)
	openFile = open(fileName, "r")
	text = openFile.read(size)
	a = text.split("\n")
	ans = []
	for i in range(len(a)):
		if a[i] != "":
			ans.append(map(float, a[i].split()))
			ans[-1] = numpy.array(ans[-1], dtype = numpy.float64)
	return numpy.array(ans)

def sigmoid(z):
	return 1.0 / (1.0 + numpy.exp(-z))

def predictOne(x, theta, network):
	a = x
	a = numpy.hstack((numpy.array([1]), a))
	for i in range(1, len(network)):
		z = (numpy.dot(a, numpy.transpose(theta[i - 1])))
		a = (sigmoid(z))
		a = numpy.hstack((numpy.array([1]), a))
	a = a[1:]
	return a.argmax() + 1



pos_x = width / 2.0
pos_y = height / 2.0

files = []

for fileName in os.listdir('resizedDuck'):
	files.append('resizedDuck/' + fileName)

for fileName in os.listdir('resizedLama'):
	files.append('resizedLama/' + fileName)

img = None
finalImage = None
w = Tkinter.Label(tk, text = "hello")
w.pack()

network = [2700, 2000, 2]

theta = []
for i in range(1, len(network)):
	theta.append(parseInput('theta' + str(i) + '.txt'))

data = parseInput('data.txt')
x = data[:, :-1]

def load():
	global finalImage
	global pos_x
	global pos_y
	global img
	global tk
	global w
	global x
	global theta
	global network

	imgs = {1: 'duck', 2: 'lama'}

	num = random.randrange(len(files))

	w.destroy()
	window.delete(finalImage)
	name = files[num]
	img = ImageTk.PhotoImage(Image.open(name).resize((500, 500)))
	finalImage = window.create_image(pos_x, pos_y, image = img)

	w = Tkinter.Label(tk, text = imgs[predictOne(x[num], theta, network)], font=("Helvetica", 50))
	w.pack()

	tk.after(1000, load)

tk.after(0, load)
tk.mainloop()