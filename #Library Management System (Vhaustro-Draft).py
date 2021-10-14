#Library Management System
#This is draft based on a software module that entails different procedures in managing a library. 
#Modules: Display, Issue, Add and Return Books.
#This modules describe the amount of books that are available (Display Books) and how many have been issued
#In addition they also capture how many have been returned and how one can add books to the Library system

#Library Managements System (Vhaustro) allows you to view and modify the books collection in correspondence 
#to contributing to the collection.

import datetime
import os
#os.getcwd()

class LMS:
    " This class purpose it to keep a record of all the books (DISPLAY) "
    " It contains 4 modules of which contribute to it's complete collection "
    " Display Books, Issue Books, Add Books, Return Books"
    def __init__(self,list_of, library_name):
            self.list_of_books = "List_of_books.txt"
            self.library_name = library_name
            self.books_dict = {}
            Id = 118
            with open(self.list_of_books) as bk:
                content = bk.readlines()
            for line in content:
                self.books_dict.update({str(Id):{'books_title':line.replace("\n",""),'lender_name':'','lend_date':'', 'status':'Available'}})
            Id += 1

#Display Books section
    def display_books(self):
        print("------------------------List of Books---------------------")
        print("Books ID","\t", "Title")
        print("----------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t", value.get("books_title"), "- [", value.get("status"),"]")

#Issue Section
    def Issue_books(self):
        books_id = input("Enter Books ID : ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['status'] == 'Available':
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['lend_date']}")
                return self.lend_books()
            elif self.books_dict[books_id]['status'] == 'Available':
                your_name = input("Enter Your Name : ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['lend_date'] = current_date
                self.books_dict[books_id]['status']= 'Already Issued'
                print("Book Issued Successfully !!!\n")
        else:
            print("Book ID Not Found !!!")
            return self.Issue_books()


#Add Books section
def add_books(self):
        new_books = input("Enter Books Title : ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 20:
            print("Books title length is too long !!! Title length limit is 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as b:
                b.writelines(f"{new_books}\n")
            self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':'','lend_date':'', 'status':'Available'}})
            print(f"The books '{new_books}' has been added successfully !!!")


#Return Books
def return_books(self):
        books_id = input("Enter Books ID : ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.return_books()
            elif not self.books_dict[books_id]['status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['lend_date'] = ''
                self.books_dict[books_id]['status']= 'Available'
                print("Successfully Updated !!!\n")
        else:
            print("Book ID Not Found !!!")
    

