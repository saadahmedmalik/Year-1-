from Book import Book

book1=Book("A Brief History of Time","Stephen Hawking",10.17,"GV5N32M9")
book2=Book("The Alchemist","P. Coelho",6.99,"TR3FL0EW")
book3=Book("Thus Spoke Zarathustra","F. Nietzsche",7.81,"F2O9PIE9")
book4=Book("Jonathan Livingston Seagull","R. Bach",6.97,"R399CED1")
book5=Book("The Time Machine","H. G. Wells",5.95,"6Y9OPL87")
book6=Book("Introduction to Programming in Python","R. Sedgewick",69.99,"5T3RRO90")
book7=Book("Atoms of Silence","H. Reeves",28.02,"3W2TB162")
book8=Book("2001: A Space Odyssey","A. C. Clarke",8.99,"TU2RL012")
book9=Book("20,000 Leagues under the Sea","J. Verne",5.99,"JI2PL986")
book10=Book("Les Miserables","V. Hugo",9.98,"VC5CE249")

class Inventory:
    def __init__(self):
        self.lob=[]

    def initialize(self):
        self.lob=self.lob+[book1]
        self.lob=self.lob+[book2]
        self.lob=self.lob+[book3]
        self.lob=self.lob+[book4]
        self.lob=self.lob+[book5]
        self.lob=self.lob+[book6]
        self.lob=self.lob+[book7]
        self.lob=self.lob+[book8]
        self.lob=self.lob+[book9]
        self.lob=self.lob+[book10]
        return self.lob
    def __str__(self):
        
        for i in range(len(self.lob)):
            print("%s - Title: %s; Author: %s; (Ref: %s; Price: $%s)" % ((i+1),self.lob[i].title,self.lob[i].author,self.lob[i].reference_number,self.lob[i].price))
        return ""
    def info(self):
    
        
        x1=len(self.lob)
        y=0
        g=0
        for i in range(len(self.lob)):
            
            y=y+self.lob[i].price
            
        for i in range(len(self.lob)):
            
            w=self.lob[i].price
            
            if g<w:
                g=w
            else:
                g=g
            
        print("#Items:",x1)
        print("Total price $%s"%(y))
        print("Most expensive itme at $%s"%(g))
    
    def search(self,a):
        k=0
        for i in range(len(self.lob)):
            if a in self.lob[i].title:
                print("%s - Title: %s; Author: %s; (Ref: %s; Price: $%s)" % ((i+1),self.lob[i].title,self.lob[i].author,self.lob[i].reference_number,self.lob[i].price))
                k=k+1
            
        if k==0:
            print("No book found!")
                

    def add(self,book=None):
        if book==None:
            new_book=Book(input("Enter Title:"),input("Enter Author Name:"),float(input("Enter price:")),input("Enter Reference Number:"))
            self.lob=self.lob+[new_book]
        elif book!=None:
            self.lob=self.lob+[book]
            print("%s added to shopping cart!"%(book.title))
    
    
            
            
            
            



    def delete(self,d):
        del self.lob[d-1]

    def adjust_price(self,roi):
        for i in range(len(self.lob)):
            self.lob[i].price=(self.lob[i].price)*(1+(roi/100))
