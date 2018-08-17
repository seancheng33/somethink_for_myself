import turtle as t

def drawSnake(rad,angle,len,neckrad):
	for i in range(len):
		t.circle(rad, angle)
		t.circle(-rad, angle)
	t.circle(rad, angle/2)
	t.fd(rad)
	t.circle(neckrad+1,180)
	t.fd(rad*2/3)

def main():
	t.setup(1300,800,0,0)
	pythonsize = 30
	t.pensize(pythonsize)
	t.pencolor('blue')
	t.seth(-40)
	drawSnake(40,80,5,pythonsize/2)
	t.done()

if __name__ == '__main__':
	main()