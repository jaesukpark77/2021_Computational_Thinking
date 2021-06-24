import turtle as t

t.shape('turtle')
t.shapesize(3)
t.color('blue')

#사각형
for i in range(4) :  
    t.forward(300)
    t.right(90)

#삼각형
for i in range(3) :  
    t.forward(300)
    t.left(120)

#오각형
for i in range(5) :  
    t.forward(300)
    t.left(72)
