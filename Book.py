class Book:
    ## to complete
    def __init__(self,title,author,price,reference_number):
        self.title=title
        self.author=author
        self.price=price
        self.reference_number=reference_number

    def __str__(self):
        return "Title: %s; Author: %s; (Ref: %s; Price: $%s)"%(self.title,self.author,self.reference_number,self.price)




def main():
    book1=Book("A Brief History of Time","Stephen Hawking",10.17,"GV5N32M9")
    print(book1)

if __name__=="__main__":
    main()
