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
            self.list_of_books = "List_of_books"