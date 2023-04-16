# -*- coding: utf-8 -*-
"""
create the program interface using tkinter buttons and pages
Created on Wed Apr  8 09:56:10 2020

@author: calpo
"""
from tkinter import *
import tkinter as tk

#create menu window of size 1080x720
root = tk.Tk()
root.title('Main Menu')
width  = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')

#Main menu text
label_menu = Label(root, text = "Main Menu", font="Segoe 22 bold")
label_menu.grid(row=0)

#quit button
quit = tk.Toplevel(root)
quitButton = tk.Button(root, text ="Quit", command = root.destroy)
quitButton.config( height = 5, width = 100, font="Segoe 18")
quitButton.grid(row=3)

#coding menu creation
def codeMenu():
   codingMenu = tk.Toplevel(root)
   codingMenu.title('Coding Menu')
   codingMenu.geometry(f'{width}x{height}')
   
   #coding menu text
   label_menu = Label(codingMenu, text = "Coding", font="Segoe 22 bold")
   label_menu.grid(row=0, column=2)
   label_opt = Label(codingMenu, text = "Choose one of the programs below:", font="Segoe 18")
   label_opt.grid(row=1, column=2)
   
   #open hello world using hello world button on code menu
   cmButton = Button(codingMenu, text ="Hello World", command = HelloWorld, font="Segoe 18")
   cmButton.grid(row=2, column=0)
   cmButton.config( height = 5, width = 30 )
   label1 = Label(codingMenu, text = " ")
   label1.grid(row=2, column=1)
   
   #open counting loop using the button on the code menu
   cmButton2 = Button(codingMenu, text ="Counting Loop", command = CountLoop, font="Segoe 18")
   cmButton2.grid(row=2, column=2)
   cmButton2.config( height = 5, width = 30 )
   label2 = Label(codingMenu, text = " ")
   label2.grid(row=2, column=3)
   
   #open calculator using button on code menu
   cmButton3 = Button(codingMenu, text ="Calculator", command = Calculator, font="Segoe 18")
   cmButton3.grid(row=2, column = 4)
   cmButton3.config( height = 5, width = 30 )
   
   #BackButton (return to the main menu)
   cmBack = Button(codingMenu, text ="Back", command = codingMenu.destroy, font="Segoe 18")
   cmBack.grid(row=4, column=2)
   cmBack.config( height = 5, width = 30 )
   
#button to open the coding menu
cMenuButton = tk.Button(root, text ="Coding", command = codeMenu)
cMenuButton.config( height = 5, width = 100, font="Segoe 18")
cMenuButton.grid(row=1)

#open help screen
def helpScreen():
   helpWindow = tk.Toplevel(root)
   helpWindow.title('Help Screen')
   helpWindow.geometry(f'{width}x{height}')
   #help title
   labelhTitle = Label(helpWindow, text = "Help", font="Segoe 22 bold")
   labelhTitle.grid(row=0, column=3)
   #text on screen
   labelhInfo = Label(helpWindow, text = "This application allows for multiple programs to be created. 3 can be chosen from.", font="Segoe 18")
   labelhInfo.grid(row=1, column=3)
   labelhInfo1 = Label(helpWindow, text = "Programs are created using the Kinect sensor and motion controls.", font="Segoe 18")
   labelhInfo1.grid(row=2, column=3)
   labelhInfo2 = Label(helpWindow, text = "Choose the correct option button for each section of the program code.", font="Segoe 18")
   labelhInfo2.grid(row=3, column=3)
   labelhInfo3 = Label(helpWindow, text = "When complete, choose the run button to test if the code works correctly.", font="Segoe 18")
   labelhInfo3.grid(row=4, column=3)
   #button to close help screen
   hBack = Button(helpWindow, text ="Back", command = helpWindow.destroy, font="Segoe 18")
   hBack.grid(row=5, column=3)
   hBack.config( height = 5, width = 30 )
   
#help button on main menu
helpButton = tk.Button(root, text ="Help", command = helpScreen)
helpButton.config( height = 5, width = 100, font="Segoe 18")
helpButton.grid(row=2)
   
#Coding Menu options
#the options available for program selection:
#open Hello World
def HelloWorld():
   hwScreen = tk.Toplevel(root)
   hwScreen.title('Hello World')
   hwScreen.geometry(f'{width}x{height}')
   
   #run button
   hwRun = Button(hwScreen, text ="Run", command = HelloWorld, font="Segoe 18")
   hwRun.config( height = 5, width = 25 )
   hwRun.grid(row=1, column=2)
   #code window
   txtHwCode = Text(hwScreen, height=28, width=45, font="Segoe 14")
   txtHwCode.grid(row=1, column=1)
   #code window
   txtHwOut = Text(hwScreen, height=28, width=45, font="Segoe 14")
   txtHwOut.grid(row=1, column=3)
   
   #option buttons
   hwOp1 = Button(hwScreen, text ="Option 1", command = HelloWorld, font="Segoe 18")
   hwOp1.config( height = 5, width = 25 )
   hwOp1.grid(row=2, column=1)
   hwOp2 = Button(hwScreen, text ="Option 2", command = HelloWorld, font="Segoe 18")
   hwOp2.config( height = 5, width = 25 )
   hwOp2.grid(row=2, column=2)
   hwOp3 = Button(hwScreen, text ="Option 3", command = HelloWorld, font="Segoe 18")
   hwOp3.config( height = 5, width = 25 )
   hwOp3.grid(row=2, column=3)
   
   #button to close hello world screen
   hwBack = Button(hwScreen, text ="Back", command = hwScreen.destroy, font="Segoe 18")
   hwBack.grid(row=3, column=1)
   hwBack.config( height = 5, width = 25 )
   
   #help button
   hwHelp = tk.Button(hwScreen, text ="Help", command = helpScreen)
   hwHelp.config( height = 5, width = 25, font="Segoe 18")
   hwHelp.grid(row=3, column=3)

#code to help with runtime of the hello world code and output
#def HwRunCode():
    
#counting program
def CountLoop():
    countScreen = tk.Toplevel(root)
    countScreen.title('Counting Loop')
    countScreen.geometry(f'{width}x{height}')
    #run button
    countRun = Button(countScreen, text ="Run", command = HelloWorld, font="Segoe 18")
    countRun.config( height = 5, width = 25 )
    countRun.grid(row=1, column=2)
    #code window
    txtCountCode = Text(countScreen, height=28, width=45, font="Segoe 14")
    txtCountCode.grid(row=1, column=1)
    #code window
    txtCountOut = Text(countScreen, height=28, width=45, font="Segoe 14")
    txtCountOut.grid(row=1, column=3)
    
    #option buttons
    countOp1 = Button(countScreen, text ="Option 1", command = HelloWorld, font="Segoe 18")
    countOp1.config( height = 5, width = 25 )
    countOp1.grid(row=2, column=1)
    countOp2 = Button(countScreen, text ="Option 2", command = HelloWorld, font="Segoe 18")
    countOp2.config( height = 5, width = 25 )
    countOp2.grid(row=2, column=2)
    countOp3 = Button(countScreen, text ="Option 3", command = HelloWorld, font="Segoe 18")
    countOp3.config( height = 5, width = 25 )
    countOp3.grid(row=2, column=3)
    
    #button to close count screen
    countBack = Button(countScreen, text ="Back", command = countScreen.destroy, font="Segoe 18")
    countBack.grid(row=3, column=1)
    countBack.config( height = 5, width = 25 )
    
    #help button
    countHelp = tk.Button(countScreen, text ="Help", command = helpScreen)
    countHelp.config( height = 5, width = 25, font="Segoe 18")
    countHelp.grid(row=3, column=3)

#code to help with runtime of the counting code and output    
#def CountRun():
    
#calculator program
def Calculator():
    calcScreen = tk.Toplevel(root)
    calcScreen.title('Calculator')
    calcScreen.geometry(f'{width}x{height}')
    #run button
    calcRun = Button(calcScreen, text ="Run", command = HelloWorld, font="Segoe 18")
    calcRun.config( height = 5, width = 25 )
    calcRun.grid(row=1, column=2)
    #code window
    txtCalcCode = Text(calcScreen, height=28, width=45, font="Segoe 14")
    txtCalcCode.grid(row=1, column=1)
    #code window
    txtCalcOut = Text(calcScreen, height=28, width=45, font="Segoe 14")
    txtCalcOut.grid(row=1, column=3)
    
    #option buttons
    calcOp1 = Button(calcScreen, text ="Option 1", command = HelloWorld, font="Segoe 18")
    calcOp1.config( height = 5, width = 25 )
    calcOp1.grid(row=2, column=1)
    calcOp2 = Button(calcScreen, text ="Option 2", command = HelloWorld, font="Segoe 18")
    calcOp2.config( height = 5, width = 25 )
    calcOp2.grid(row=2, column=2)
    calcOp3 = Button(calcScreen, text ="Option 3", command = HelloWorld, font="Segoe 18")
    calcOp3.config( height = 5, width = 25 )
    calcOp3.grid(row=2, column=3)
    
    #button to close calc screen
    calcBack = Button(calcScreen, text ="Back", command = calcScreen.destroy, font="Segoe 18")
    calcBack.grid(row=3, column=1)
    calcBack.config( height = 5, width = 25 )
    
    #help button
    calcHelp = tk.Button(calcScreen, text ="Help", command = helpScreen)
    calcHelp.config( height = 5, width = 25, font="Segoe 18")
    calcHelp.grid(row=3, column=3)

#code to help with runtime of the calculator code and output    
#def CalcRun():
    
root.mainloop()