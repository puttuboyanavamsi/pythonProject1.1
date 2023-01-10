import tkinter
from tkinter import*
root=tkinter.Tk()
from tkinter import messagebox
def ok():
    username=username_entry .get()
    password=password_entry.get()
    if(username==""and password==""):
        messagebox .showinfo("", "emptyblocks not allowed")
    elif(username =="vamsi" and password=="12345"):
        messagebox .showinfo("","sucessfully login")
    else:
        messagebox.showinfo("","incorrectdetails")
root .title("welcome to instragram")
root.geometry("600x600")
global username_entry
global password_entry
label=Label (root,text="login to instragram",font= "areial 40 bold",bg="red",fg="black").pack(fill='both')
label=Label (root,text="username",font= "40").place (x=100,y=130)
label=Label (root,text="password",font= "40").place(x=100,y=160)
username_entry=Entry (root,font= "40")
username_entry .place (x=180,y=130)
password_entry=Entry (root,font="40")
password_entry.place(x=180,y=160)
b=Button (root ,text="login",command=ok, font= "80",bg="white",fg="black")
b.place (x=220,y=200)
root.mainloop()



