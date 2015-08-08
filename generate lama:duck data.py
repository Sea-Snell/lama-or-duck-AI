from PIL import Image
import os

w = 30
h = 30

openFile = open('testData.txt', "w+")
openFile.truncate()

for fileName in os.listdir('testDuck'):
	if fileName != '.DS_Store':
		Image.open('testDuck/' + fileName).resize((w, h), Image.ANTIALIAS).save('testResizedDuck/' + fileName)

for fileName in os.listdir('testLama'):
	if fileName != '.DS_Store':
		Image.open('testLama/' + fileName).resize((w, h), Image.ANTIALIAS).save('testResizedLama/' + fileName)

for fileName in os.listdir('testResizedDuck'):
	if fileName != '.DS_Store':
		loadedImage = Image.open('testResizedDuck/' + fileName).load()
		for x in range(w):
			for y in range(h):
				openFile.write(str(loadedImage[x, y][0]) + ' ' + str(loadedImage[x, y][1]) + ' ' + str(loadedImage[x, y][2]) + ' ')
		openFile.write('1')
		openFile.write('\n')

for fileName in os.listdir('testResizedLama'):
	if fileName != '.DS_Store':
		loadedImage = Image.open('testResizedLama/' + fileName).load()
		for x in range(w):
			for y in range(h):
				openFile.write(str(loadedImage[x, y][0]) + ' ' + str(loadedImage[x, y][1]) + ' ' + str(loadedImage[x, y][2]) + ' ')
		openFile.write('2')
		openFile.write('\n')
