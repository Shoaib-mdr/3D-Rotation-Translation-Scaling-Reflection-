from tkinter import *
from math import sqrt

print("Enter the WIDTH, HEIGHT AND LENGTH of the CUBE")
width,height,length=map(int,input().split())
print ("enter the Center Of Cordinates Xcentre Ycentre")
Xcentre,Ycentre=map(int,input().split())
Zcentre=0
master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
canvas=Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
pnts=[]
def CVT3to2(x,y,z):
	z=z/sqrt(2)
	x=ox+(x-z)
	y=oy-(y-z)
	return x,y

def CreateCube(pnts3d,outline='black'):
	for i in range (len(pnts3d)):	
		pnts.insert(i,CVT3to2(pnts3d[i][0],pnts3d[i][1],pnts3d[i][2]))
	canvas.create_rectangle(pnts[0],pnts[2],outline=outline)	
	canvas.create_rectangle(pnts[4],pnts[6],outline=outline)	
	canvas.create_line(pnts[0],pnts[4],fill=outline)
	canvas.create_line(pnts[1],pnts[5],fill=outline)
	canvas.create_line(pnts[2],pnts[6],fill=outline)
	canvas.create_line(pnts[3],pnts[7],fill=outline)	

def reflection(x,y,z):
	ReflectionY=   [[1, 0, 0, 0],
		 [0, -1, 0, 0],
		 [0, 0, 1, 0],
		 [0, 0, 0, 1]]

	P =     [[x],
		[y],
		[z],
		[1]]

	resulty= [[0],
	  	 [0],
	   	 [0],
		 [0]]
	for i in range(len(ReflectionY)):
		for j in range(len(P[0])):
			for k in range(len(P)):
				resulty[i][j] += ReflectionY[i][k] * P[k][j]
	return resulty[0][0],resulty[1][0],resulty[2][0]
ox,oy=canvas_width/2,canvas_height/2
canvas.create_line(ox,0,ox,oy)
canvas.create_line(ox,oy,ox*2,oy)
canvas.create_line(ox,oy,0,oy*2)
pnts3d=[(0,0,0),(width,0,0),(width,height,0),(0,height,0),(0,0,length),(width,0,length),(width,height,length),(0,height,length)]
pnts3dnew=[]
for i in range(len(pnts3d)):
	pnts3dnew.insert(i,(pnts3d[i][0]+Xcentre,pnts3d[i][1]+Ycentre,pnts3d[i][2]+Zcentre))
CreateCube(pnts3dnew)
pntsx=[]
for i in range(len(pnts)):
	pntsx.insert(i,reflection(pnts3dnew[i][0],pnts3dnew[i][1],pnts3dnew[i][2]))
CreateCube(pntsx,'green')
mainloop()




     
