from tkinter import *
from math import sqrt
from math import sin, cos, radians, pi
print("Enter the WIDTH, HEIGHT, and LENGTH of Cube")
width,height,lenght=map(int,input().split())
print ("enter the Center of Coordinate XCenterenter,YCenterenter")
XCenter,YCenter=map(int,input().split())
ZCenter=0
print("Enter Rotation Angle")
theta=float(input())
theta=radians(theta)
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
	canvas.create_polygon(points[0],points[1],points[2],points[3],outline=outline,fill='')	
	canvas.create_polygon(points[4],points[5],points[6],points[7],outline=outline,fill='')	
	canvas.create_line(points[0],points[4],fill=outline)
	canvas.create_line(points[1],points[5],fill=outline)
	canvas.create_line(points[2],points[6],fill=outline)
	canvas.create_line(points[3],points[7],fill=outline)	

def Rotation(x,y,z):
	RotationZ = 	[[cos(theta), -sin(theta), 0,	0],
      		[sin(theta), cos(theta),  0,	0],
      		[0,              0,        1,	0],
		[0,		0,	0,	1]]

	P =     [[x],
		[y],
		[z],
		[1]]

	result= [[0],
	  	 [0],
	   	 [0],
		 [0]]
	for i in range(len(RotationZ)):
		for j in range(len(P[0])):
			for k in range(len(P)):
				result[i][j] += RotationZ[i][k] * P[k][j]
	return result[0][0],result[1][0],result[2][0]
ox,oy=canvas_width/2,canvas_height/2
canvas.create_line(ox,0,ox,oy)
canvas.create_line(ox,oy,ox*2,oy)
canvas.create_line(ox,oy,0,oy*2)
points3d=[(0,0,0),(width,0,0),(width,height,0),(0,height,0),(0,0,lenght),(width,0,lenght),(width,height,lenght),(0,height,lenght)]
New3dPOINTS=[]
for i in range(len(points3d)):
	New3dPOINTS.insert(i,(points3d[i][0]+XCenter,points3d[i][1]+YCenter,points3d[i][2]+ZCenter))
CreateCube(New3dPOINTS)
pointsx=[]
for i in range(len(points)):
	pointsx.insert(i,Rotation(New3dPOINTS[i][0],New3dPOINTS[i][1],New3dPOINTS[i][2]))
print (pointsx)
CreateCube(pointsx,'green')
mainloop()




     
