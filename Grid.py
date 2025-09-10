from tkinter import *
from Pixel import Pixel
import numpy as np
import random, time


class Grid:
      


### To complete
        
        
        def __init__(self,root,i,j,scale):
        
                self.i=i
                self.j=j
                self.scale=scale
                self.canvas=Canvas(root,width=j*scale,height=i*scale)
                self.canvas.pack()
                self.create_grid()
                self.matrix=(np.zeros((i,j)))
                self.w_pix=[]
                self.p_pix=[]
                
        

        def create_grid(self):
               pixss=[]
               

               for p in range(self.i):
                       for x in range (self.j):
                              pixss.append(Pixel(self.canvas,p,x,self.j,self.i,self.scale,0))
                        

        def random_pixels(self,num_pix,color):
               
               for i in range(num_pix):
                      x=np.random.randint(0,self.j)
                      p=np.random.randint(0,self.i)
                      self.addij(x*self.scale,p*self.scale,color)
                      
                
                      
                      
        def addxy(self,x,y):
               
               print("insert",x,y,x//self.j,y//self.i,self.matrix[y//self.scale,x//self.scale])
               self.addij(x,y,1)
               
               

        def delxy(self,x,y):
               print("delete",x,y,x//self.j,y//self.i,self.matrix[y//self.scale,x//self.scale])
               self.delij(x,y)

               
               
        def delij(self,i,j):
               
               
        

               if self.matrix[j//self.scale,i//self.scale]==1.0:
                      
                      self.matrix[j//self.scale,i//self.scale]=0.0
                      self.reset()
               elif self.matrix[j//self.scale,i//self.scale]==0.0:
                      n=j//self.scale
                      
                
                      self.flush_row(n)

        def addij(self,j,i,c):
               
               self.w_pix.append(Pixel(self.canvas,i//self.scale,j//self.scale,self.j,self.i,self.scale,c))
               self.matrix[i//self.scale,j//self.scale]=1
               
        def reset(self):
               for pixel in self.w_pix:
                      Pixel.delete(pixel)
               
               for i in range(self.i):
                for j in range(self.j):
                   if self.matrix[i,j]==1.0:
                        self.addij(j*self.scale,i*self.scale,1)

        def flush_row(self,i):
              
         for l in range(3):
                    self.p_pix.append(Pixel(self.canvas,i,l,self.j,self.i,self.scale,7,[0,1]))
                    
         for r in range(3):
                    self.p_pix.append(Pixel(self.canvas,i,self.j-r,self.j,self.i,self.scale,7,[0,-1]))
         for h in range(14):
                for p in self.p_pix :
                  
                  p.next()
                  
                self.canvas.update()
                time.sleep(0.02)
         for p in self.p_pix:
                Pixel.delete(p)
         for items in self.matrix[i,:]:
                if items==1.0:      
                        items=0.0
         #self.matrix=np.delete(self.matrix,i,0)
         self.matrix[1:i+1,:]=self.matrix[0:i,:]
         self.matrix[0,:]=0.0
         self.reset()
         


        
                
         
         
         
         
         

        
                

              

               
               
               

               




#########################################################
############# Main code #################################
#########################################################

  
def main(): 
        
        ##### create a window, canvas 
        root = Tk()                # instantiate a tkinter window
        mesh = Grid(root,50,30,20) # instantiate a Grid object
        mesh.random_pixels(25,1) # generate 25 random (white) pixels in the Grid

        
        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:mesh.addxy(e.x,e.y))
        root.bind("<Button-2>",lambda e:mesh.delxy(e.x,e.y))
        root.bind("<Button-3>",lambda e:mesh.delxy(e.x,e.y))
        

        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

