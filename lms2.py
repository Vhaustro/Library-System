from tkinter import *

#An introduction into the Graphical User Interface
#Label widget
root = Tk()

#Creating the widget/programme
#vhaustroLablel = Label(root, text= "Bonjour de Monde.")
#vhaustroLablel2 = Label(root, text="Je m'appelle Vhaustro")

def myClick():
    vhaustroButton = Label(root, text="Wow, such a beautiful button!!")
    vhaustroButton.pack()

vhaustroButton = Button(root, text="Click to Proceed", command=myClick())
vhaustroButton.pack()





#Display on the screen
#vhaustroLablel.grid(row=39, column=7)
#vhaustroLablel2.grid(row=9, column=7)

#EventLoop- Porgramme that keeps on restarting itself continuously and keeps a record of the activity within that Label
#EventLoop - Keeps it running until we use/close it
 
root.mainloop()

#Grid system
#All programmes have rows and columns known as grids
#Starting with zero within horizontal/vertical division of a page it stretches out but
#determined by the intended size of the program


class library:
    def __init__(self,listofbooks)
    self.availablebooks=listofbooks


    def displayAvailablebooks=
    
