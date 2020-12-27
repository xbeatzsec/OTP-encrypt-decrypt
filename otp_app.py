#!/usr/bin/python3
import onetimepad      
from tkinter import * 
import time
import os
from PIL import Image, ImageTk

cifrar = onetimepad
os.system("clear")
print("-----------------------------------------------------------------")
print("")
time.sleep(0.1)
print("     OOOOOOOOO     TTTTTTTTTTTTTTTTTTTTTTTPPPPPPPPPPPPPPPPP" )   
time.sleep(0.1)  
print("   OO:::::::::OO   T:::::::::::::::::::::TP::::::::::::::::P")  
time.sleep(0.1)     
print(" OO:::::::::::::OO T:::::::::::::::::::::TP::::::PPPPPP:::::P ")   
time.sleep(0.1)  
print("O:::::::OOO:::::::OT:::::TT:::::::TT:::::TPP:::::P     P:::::P ")
time.sleep(0.1)  
print("O::::::O   O::::::OTTTTTT  T:::::T  TTTTTT  P::::P     P:::::P ") 
time.sleep(0.1)   
print("O:::::O     O:::::O        T:::::T          P::::P     P:::::P ")  
time.sleep(0.1)  
print("O:::::O     O:::::O        T:::::T          P::::PPPPPP:::::P " )  
time.sleep(0.1)  
print("O:::::O     O:::::O        T:::::T          P:::::::::::::PP ") 
time.sleep(0.1)     
print("O:::::O     O:::::O        T:::::T          P::::PPPPPPPPP")   
time.sleep(0.1)      
print("O:::::O     O:::::O        T:::::T          P::::P   ") 
time.sleep(0.1)             
print("O:::::O     O:::::O        T:::::T          P::::P  ")
time.sleep(0.1)              
print("O::::::O   O::::::O        T:::::T          P::::P  ") 
time.sleep(0.1)              
print("O:::::::OOO:::::::O      TT:::::::TT      PP::::::PP  " )  
time.sleep(0.1)          
print(" OO:::::::::::::OO       T:::::::::T      P::::::::P  " )
time.sleep(0.1)            
print("   OO:::::::::OO         T:::::::::T      P::::::::P  " )  
time.sleep(0.1)          
print("     OOOOOOOOO           TTTTTTTTTTT      PPPPPPPPPP ")
time.sleep(0.1)
print("")
print("        ONE                 TIME              PAD")
print("")
time.sleep(0.1)
print("-----------------------------------------------------------------")
print("")
print("")
text = str(input("Enter your message: "))
print("")
key = str(input("Insert the key that you want: "))
while len(key) < len(text):
	os.system("clear")
	print("The key is minor than your message!")
	print("")
	print("Encryption can be compromised...")
	print("")
	print("Try again!")
	key = str(input("Insert the key that you want: "))
while key == "":
	os.system("clear")
	print("")
	print("None key was inserted")
	print("")
	print("Try again!")
	time.sleep(0.5)
	key = str(input("Inserir the key: "))


print("")
print("Opening the encryption system.....")
time.sleep(2)


root = Tk() 
root.title("One Time Pad Cipher") 
root.geometry("600x600")
load = Image.open("images/image.jpg")
render = ImageTk.PhotoImage(load)
background = Label(root, image=render)
background.place(x=0, y=0)
background.place(x=0, y=0, relwidth=1, relheight=1)


def mensagemEncrypt():
    input_user_1 = entrada1.get()

  
    c = cifrar.encrypt(input_user_1, key) 
    entrada2.insert(0, c) 

def mensagemDecrypt():                      
    input_user_3 = entrada3.get() 
  
    d = cifrar.decrypt(input_user_3, key)
    entrada4.insert(0, d)

label1 = Label(root, text ='Plain text')                
label1.grid(row = 10, column = 1) 
label2 = Label(root, text ='Encrypted text') 
label2.grid(row = 11, column = 1) 
l3 = Label(root, text ="Encrypted text") 
l3.grid(row = 10, column = 10) 
l4 = Label(root, text ="Decrypted Text") 
l4.grid(row = 11, column = 10)

  

entrada1 = Entry(root) 
entrada1.grid(row = 10, column = 2) 
entrada2 = Entry(root) 
entrada2.grid(row = 11, column = 2) 
entrada3 = Entry(root) 
entrada3.grid(row = 10, column = 11) 
entrada4 = Entry(root) 
entrada4.grid(row = 11, column = 11) 


  

ent = Button(root, text = "Encrypt", bg ="red", fg ="white", command = mensagemEncrypt) 
ent.grid(row = 13, column = 2)
  

b2 = Button(root, text = "Decrypt", bg ="green", fg ="white", command = mensagemDecrypt) 
b2.grid(row = 13, column = 11) 
  

root.mainloop()
