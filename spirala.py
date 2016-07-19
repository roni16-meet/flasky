import turtle
import math
z=1
for x in range (1, 100000):
	turtle.goto(math.cos(x),math.sin(x))
	z=z*1.000001
turtle.mainloop()
