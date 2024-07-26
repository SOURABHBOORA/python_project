from tkinter import *

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image (args:100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label =Label(text="Website")
website_label.grid(row=1,column=0)
website_label =Label(text="Email/Username")
website_label.grid(row=2,column=0)
website_label =Label(text="Password")
website_label.grid(row=3,column=0)

#Entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
window.mainloop()
