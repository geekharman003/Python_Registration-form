from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Sr no",width=20,font=("bold", 10))
label_1.place(x=66,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Name",width=20,font=("bold", 10))
label_2.place(x=66,y=160)

entry_2 = Entry(root)
entry_2.place(x=240,y=160)

label_2 = Label(root, text="URN",width=20,font=("bold", 10))
label_2.place(x=66,y=190)

entry_2 = Entry(root)
entry_2.place(x=240,y=190)

label_3 = Label(root, text="Address",width=20,font=("bold", 10))
label_3.place(x=66,y=220)

entry_2 = Entry(root)
entry_2.place(x=240,y=220)

label_5=Label(root,text="Branch",width=20,font=("bold",10))
label_5.place(x=66,y=250)
list_of_branches=[ 'CSE' ,'IT','Electrical','ECE' ,'Mechanical' ,'Civil']
c=StringVar()
droplist=OptionMenu(root,c, *list_of_branches)
droplist.config(width=15)
c.set('Select your branch')
droplist.place(x=240,y=250)

label_6 =Label(root,text="Gender", width=20,font=("bold",10))
label_6.place(x=66,y=290)


var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=240,y=290)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=299,y=290)

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=150,y=380)
root.configure(background = "skyblue")
root.mainloop()
print("registration form created")