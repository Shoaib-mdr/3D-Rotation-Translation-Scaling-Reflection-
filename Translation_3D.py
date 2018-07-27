from tkinter import *
from math import sqrt
from math import sin, cos, radians, pi
print("Enter the WIDTH, HEIGHT, and LENGTH of Cube")
width,height,lenght=map(int,input().split())
print ("enter the Center of Coordinate XCenter,YCenter")
XCenter,YCenter=map(int,input().split())
ZCenter=0
print("Translation Factor: tx, ty, tz")
tx,ty,tz=map(int,input().split())
master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
canvas=Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
points=[]
def CVT3to2(x,y,z):
	z=z/sqrt(2)
	x=ox+(x-z)
	y=oy-(y-z)
	return x,y

def CreateCube(points3d,outline='black'):
	for i in range (len(points3d)):	
		points.insert(i,CVT3to2(points3d[i][0],points3d[i][1],points3d[i][2]))
		canvas.create_text(points[i],text=str(i),font="Times 10 bold")
	print (str(points)+"\n")
	canvas.create_rectangle(points[0],points[2],outline=outline)	
	canvas.create_rectangle(points[4],points[6],outline=outline)	
	canvas.create_line(points[0],points[4],fill=outline)
	canvas.create_line(points[1],points[5],fill=outline)
	canvas.create_line(points[2],points[6],fill=outline)
	canvas.create_line(points[3],points[7],fill=outline)	

def Translation(x,y,z):
	T = 	[[1, 0, 0, tx],
		 [0, 1, 0, ty],
		 [0, 0, 1, tz],
		 [0, 0, 0, 1]]
	P =     [[x],
		[y],
		[z],
		[1]]

	result= [[0],
	  	 [0],
	   	 [0],
		 [0]]
	for i in range(len(T)):
		for j in range(len(P[0])):
			for k in range(len(P)):
				result[i][j] += T[i][k] * P[k][j]
	return result[0][0],result[1][0],result[2][0]
ox,oy=canvas_width/2,canvas_height/2
canvas.create_line(ox,0,ox,oy)
canvas.create_line(ox,oy,ox*2,oy)
canvas.create_line(ox,oy,0,oy*2)
points3d=[(0,0,0),(width,0,0),(width,height,0),(0,height,0),(0,0,lenght),(width,0,lenght),(width,height,lenght),(0,height,lenght)]
N3DPoints=[]
for i in range(len(points3d)):
	N3DPoints.insert(i,(points3d[i][0]+XCenter,points3d[i][1]+YCenter,points3d[i][2]+ZCenter))
CreateCube(N3DPoints)
pointsx=[]
for i in range(len(points)):
	pointsx.insert(i,Translation(N3DPoints[i][0],N3DPoints[i][1],N3DPoints[i][2]))
print (pointsx)
CreateCube(pointsx,'green')
mainloop()




     
