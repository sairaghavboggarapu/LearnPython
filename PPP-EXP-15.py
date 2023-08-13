from tkinter import *
root =Tk()
root.title('MATLAB WORKSPACE')
root.geometry('400x300')
frame=Frame(root)
Label(frame,text='LOGIN TO YOUR ACCOUNT',font=('Arial Bold',16))\
.grid(row=0,column=0,columnspan=2,pady=(0,20))
Label(frame,text='User Name').grid(row=1,column=0)
Entry(frame).grid(row=1, column=1)
Label(frame,text='Password').grid(row=2,column=0)
Entry(frame).grid(row=2, column=1)
Checkbutton(frame,text='I agree to terms & condition').grid(row=3,column=0,columnspan=2,sticky=W)
Label(frame,text='LOGIN',font=('Arial Bold',12))\
.grid(row=4,column=0,columnspan=2,pady=(0,20))
frame.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
