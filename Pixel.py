from tkinter import *
import time
import random
#names
#Patrick Nugent
#Saad Malik

class Pixel:
    color=['black','white','yellow','red','blue','green','orange','purple','brown','cyan']
    vector=[0,0]
    
    ### to complete        
    def __init__(self,canvas,i_cord,j_cord,number_row=0,number_col=0,scale=0,color_id_number=0,vector=[0,0]):
        if i_cord>number_col:
            i_cord=i_cord%number_col
        if j_cord>number_row:
            j_cord=j_cord%number_row
        
        self.canvas=canvas
        self.j_cord=j_cord
        self.i_cord=i_cord
        self.nrow=number_row
        self.ncol=number_col
        self.scale=scale
        self.cid=self.color[color_id_number]
        self.rectangle=self.canvas.create_rectangle(j_cord*scale,i_cord*scale,((j_cord)*scale)+scale,((i_cord)*scale)+scale,fill=self.color[color_id_number])
        self.vector=vector
        
        
    def __str__(self):
        return "(%s,%s) %s"%(self.i_cord,self.j_cord, self.cid),(str(self.rectangle))
    
    def set_vector(self,i=0,j=0):
        self.vector=[i,j]

    def left(self):
        self.set_vector(0,-1)

    def right(self):
        self.set_vector(0,1)

    def up(self):
        self.set_vector(-1,0)

    def down(self):
        self.set_vector(1,0)

    def set_vector(self,x,y):
        self.vector=[x,y]
        
    

    def next(self):
       
       self.i_cord=self.i_cord+self.vector[0]
       self.j_cord=self.j_cord+self.vector[1]
       self.canvas.move(self.rectangle,self.vector[1]*self.scale,self.vector[0]*self.scale)

       
       
       if self.i_cord<=-1:
           self.i_cord=self.ncol
           self.canvas.moveto(self.rectangle,self.j_cord*self.scale,40*self.scale)
       elif self.i_cord>=self.ncol:
           self.i_cord=0
           self.canvas.moveto(self.rectangle,self.j_cord*self.scale,0)

       if self.j_cord<=-1:
           self.j_cord=self.nrow
           self.canvas.moveto(self.rectangle,(40*self.scale)+self.scale,(self.i_cord*self.scale))

       elif self.j_cord>=self.nrow:
           self.j_cord=0
           self.canvas.moveto(self.rectangle,0,(self.i_cord*self.scale))
       return self
    

    def delete(self):
        self.canvas.delete(self.get_id())

    def get_id(self):
        return self.rectangle

















        
#################################################################
########## TESTING FUNCTION
#################################################################
def delete_all(canvas):
    canvas.delete("all")
    print("Delete All")


def test1(canvas,nrow,ncol,scale):
    print("Generate 10 points at random")
    random.seed(4) # for reproducibility
    for k in range(10):
        i=random.randint(0,nrow-1) 
        j=random.randint(0,ncol-1)
        c=random.randint(1,9)    # color number
        pix=Pixel(canvas,i,j,nrow,ncol,scale,c)
        print(pix)

def test2(canvas,nrow,ncol,scale):
    print("Generate 10 points at random (using modulo)")
    random.seed(5) # for reproducibility
    for k in range(10):
        i=random.randint(0,nrow-1)*34
        j=random.randint(0,ncol-1)*13
        ij=str(i)+","+str(j)
        c=random.randint(1,9)    # color number
        pix=Pixel(canvas,i,j,nrow,ncol,scale,c)
        print(ij,"->",pix)

        
def test3(root,canvas,nrow,ncol,scale):
    print("Move one point along a square")

    pix=Pixel(canvas,35,35,nrow,ncol,scale,3)
    pix.vector=[-1,0] # set up direction (up)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)

        
        
    pix.vector=[0,-1] # set up new direction (left)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
        
    pix.vector=[1,0]   # set up new direction (down)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
        
    pix.vector=[0,1]    # set up new direction (right)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        

    #delete point
    pix.delete()


  
def test4(root,canvas,nrow,ncol,scale):
    print("Move four point along a square")

    pixs=[]
    pixs.append(Pixel(canvas,35,35,nrow,ncol,scale,3,[-1,0]))
    pixs.append(Pixel(canvas,5,35,nrow,ncol,scale,4,[0,-1]))
    pixs.append(Pixel(canvas,5,5,nrow,ncol,scale,5,[1,0]))
    pixs.append(Pixel(canvas,35,5,nrow,ncol,scale,6,[0,1]))
    
    print("Starting coords")
    for p in pixs: print(p)

    for i in range(30):
        for p in pixs:
            p.next()       # next move in the simulation    
        root.update()      # update the graphic
        time.sleep(0.05)   # wait in second (simulation)

    print("Ending coords")
    for p in pixs:
        print(p)
        p.delete()


        
def test5(root,canvas,nrow,ncol,scale):
    print("Move one point any direction -use arrow commands")

    pix=Pixel(canvas,20,20,nrow,ncol,scale,2)

    ### binding used by test5
    root.bind("<Right>",lambda e:pix.right())
    root.bind("<Left>",lambda e:pix.left())
    root.bind("<Up>",lambda e:pix.up())
    root.bind("<Down>",lambda e:pix.down())

    ### simulation
    while True:
        
        pix.next()
        root.update()     # update the graphic
        time.sleep(0.05)  # wait in second (simulation)



        

###################################################
#################### Main method ##################
###################################################


def main():
       
        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        nrow=40
        ncol=40
        scale=20
        canvas = Canvas(root,width=ncol*scale,height=nrow*scale,bg="black") # create a canvas width*height
        canvas.pack()

        ### general binding events to choose a testing function
        root.bind("1",lambda e:test1(canvas,nrow,ncol,scale))
        root.bind("2",lambda e:test2(canvas,nrow,ncol,scale))
        root.bind("3",lambda e:test3(root,canvas,nrow,ncol,scale))
        root.bind("4",lambda e:test4(root,canvas,nrow,ncol,scale))
        root.bind("5",lambda e:test5(root,canvas,nrow,ncol,scale))
        root.bind("<d>",lambda e:delete_all(canvas))
        
       
        
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

