import turtle

def tree(plist, l, a, f):
    if l >5:
        lst = []
        for p in plist:
            p.forward(1)
            q=p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst,1*f,a,f)

def main():
    p = Turtle()
    p.color('green')
    p.pensize(5)
    p.hideturtle()
    p.getscreen().tracer(30,0)
    p.left(90)
    p.penup()
    p.goto(x, y)
    p.pendown()
    p = tree([p], 110, 65, 0.6375)

if __name__ == '__main__':
	main()
