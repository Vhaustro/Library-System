
#Library Management System 2.0

#This library system has two classes.
#One is the Library which involves collection of books, provision of books, contributing to the current inventory.
#The second is the requests from students (to borrow a book), returning the book
#It is with great importance that I have successfully implemented this two aspects together onto this program to execute
#To produce a Library Management System

#Insert greeting (goodmorning, time depending on day), 
# (asks you if admin, or student) enter username or password
#Welcome admin/student 
#Admin: Veiw book, add books, remove books, borrowed books, view students, (4 students)
#Student: Borrow a new book, Return Book, View books borrowed

print("Welcome to Vhaustro's Library Managment System")

import datetime
from typing import MutableMapping
now = datetime.datetime.now()
print("Currently it's:")
print(now.strftime(" %H:%M: %p"))
#Remove date and automatically include time of day

if (now.strftime("%p") == "AM"):
     print("Good Morning!")
elif (now.strftime("%p") == "PM"):
     print("Good Afternoon!")
else:
    print ("Good Evening")

#Asks for name (before figuring if admin or student)
name = input ("What is your name?" + str(v = input("> "))
try:
    _ = int(v)
except:
    pass
else:
    raise ValueError("input supplied should be of type 'str'"))

#Accept text/reject numbers
#No input of undefined names, print statement to direct this message to them.
v = input("> ")
try:
    _ = int(v)
except:
    pass
else:
    raise ValueError("input supplied should be of type 'str'")



print ("Hey" + str(name) + ", " + "What gender are you?")

print ("""
Pick One:
a: Male
b. Female
c. Intersex""")

gender = input()

a = "Male"
b = "Female"
c = "Intersex"

if (gender == "Male" or a):
    print("Hey Mr. " + str(name) + ", welcome back")
elif (gender == "Female" or b):
    print ("Hi Mrs. " + str(name) + ", welcome back")
elif (gender == "Intersex" or c):
    print ("Hello," + str(name) + ", welcome back")
else:
    print ("Sorry, Kindly Try Again" + str(name))



position = input("So" + str(name) + ", are you an Admin or Student?")

role1 = "Adminitrator"
role2 = "Student"

if (position == "Administrator" or role1):
    print ("Welcome back Admin")
elif (position == "Student" or role2):
    print ("Welcome Student")
else:
    print ("OOopsies, you are NOT part of our system. Kindly checkback later")







#class Library:
    #def __init__(self, listofbooks):
     #self.availablebooks=listofbooks
    
    #def displayavailablebooks(self):
        #print("The books we have in our library are:")
        #for book in self.availablebooks:
            #print(book)
    
    #def lendbook(self,requestedbook):
        #if requestedbook in self.availablebooks:
            #print("Hazzaaaah!! You have successfully borrowed it")
        #else:
            #print("Ooopsiees!! This book is not in our inventory")


#class Student:
    #def requestbook(self):
        #print("Kindly enter the name of the book you would love to check out.")
        #self.book = input ()
        #return self.book
        
    #def returnbook (self):
        #print("Enter the name of the book you would love to return")
        #self.book = input ()
        #return self.book

#def main():
    #library= Library(["Percy Jackson and the King of the Seas" "Purple Hibiscus" "Lucas Yates: Become the Viper" "Attack on Titan: The Tale of Eren Yeager"])

    #student= Student()

    #done= False
    #while done == False:
        #print("""~~~~~Library Inventory~~~~~
        #1. View all books in our Inventory
        #2. Request a book  
        #3. Return a book
        #4. Exit""")

        #choice=int(input("Enter Choice"))
        #if choice==1:
            #library.displayavailablebooks()
        #elif choice==2:
            #library.lendbook(student.requestbook())
        #elif choice==3:
            #library.addbook(student.returnbook())
        #elif choice==4:
            #SystemExit.exit()

#main()

