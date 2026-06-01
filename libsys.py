class librasys():
    def __init__(self):
        self.file="libras.txt"
    def add_book(self):
        try:
            with open(self.file,"r") as f:
                books=f.readlines()
        except:
            books=[]
        book_id= 100+len(books)+1
        book_title=input("enter book tile:")
        author=input("enter the author name:")
        status="Available"
        record = (str(book_id)+","+book_title+","+author+","+status+"\n")
        with open (self.file,"a") as f:
            f.write(record)
        print("Book added successfully")
    def view_books(self):
        with open(self.file,"r") as f:
            books=f.readlines()
        if not books:
            print("no books to view")
            return
        print("LIST OF BOOKS")
        for book in books:
            if book.strip()=="":
                continue
            i,t,a,s=book.strip().split(",")
            print("\nbook id:",i,"\nbook title:",t,"\nAuthor:",a,"\nStatus",s,"\n")
    def search_books(self):
        book_title=input("Enter book title:")
        with open(self.file,"r") as f:
            books=f.readlines()
        found=False
        for book in books:
            if book.strip()=="":
                continue
            i,t,a,s=book.strip().split(",")
            if t==book_title:
                print("\nbook id:",i,
                      "\nbook title:",t,
                      "\nAuthor:",a,
                      "\nStatus:",s,"\n")
                found=True
        if not found:
            print("no book tittle found")
    def issue_book(self):
        book_id=input("Enter book id:")
        with open (self.file,"r") as f:
            books=f.readlines()
        issue=[]
        found=False
        for book in books:
            if book.strip()=="":
                continue
            i,t,a,s=book.strip().split(",")
            if i==book_id:
                b="Issued"
                issue.append(str(i)+","+t+","+a+","+b+"\n")
                print("book issued successfully")
                found=True
                
            else:
                issue.append(book)
        with open(self.file,"w") as f:
            f.writelines(issue)
            
        if not found:
            print("invalid book id")
    def return_book(self):
        book_id=input("enter book id:")
        with open(self.file,"r") as f:
            books=f.readlines()
            returns=[]
            found=False
            for book in books:
                if book.strip()=="":
                    continue
                i,t,a,s=book.strip().split(",")
                if i==book_id:
                    c="Available"
                    returns.append(str(i)+","+t+","+a+","+c+"\n")
                    print("book returned successfully")
                    found=True
                else:
                    returns.append(book)
            with open(self.file,"w") as f:
                f.writelines(returns)
            if not found:
                print("invalid book id")
    def delete_book(self):
        book_id=input("enter book id:")
        with open (self.file,"r") as f:
            books=f.readlines()
            delete=[]
            found=False
            for book in books:
                if book.strip()=="":
                    continue
                i,t,a,s,=book.strip().split(",")
                if i==book_id:
                    print("book deleted successfully")
                    found=True
                
                else:
                    delete.append(book)
            with open (self.file,"w") as f:
                f.writelines(delete)
            if not found:
                print("invalid book id")
system= librasys()
while True:
    print("\n LIBRARY  MANAGEMENT SYSTEM")
    print("1.add book")
    print("2.view book")
    print("3.search book")
    print("4.issue book")
    print("5.return book")
    print("6.delete book")
    print("7.EXIT")
    choice=input("enter your choice:")
    if choice=="1":
        system.add_book()
    elif choice=="2":
        system.view_books()
    elif choice=="3":
        system.search_books()
    elif choice=="4":
        system.issue_book()
    elif choice=="5":
        system.return_book()
    elif choice=="6":
        system.delete_book()
    elif choice=="7":
        print("------------Exiting STUDENT MANAGEMENT SYSTEM------------------")
        break
    else :
        print("invalid choice :(")


            
                
