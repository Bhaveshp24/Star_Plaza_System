from tkinter import*
from typing_extensions import Self
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | created by Bhavesh Patil")
        self.root.config(bg="#352F44")
        self.root.focus_force()

        self.var_invoice=StringVar()

  #========title==============
        lbl_title=Label(self.root,text="Customer Bill",font=("goudy old style",30),bg="#4d636d",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
       
        lbl_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15),bg="#352F44",fg="white").place(x=50,y=100)

        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("goudy old style",15)).place(x=160,y=100,width=180,height=28)

        btn_search=Button(self.root,text="Search",font=("time new roman",15,"bold"),bg="#DBD8E3",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="Clear",font=("time new roman",15,"bold"),bg="#DBD8E3",cursor="hand2").place(x=490,y=100,width=120,height=28)

    #=======bill list==============
        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=140,width=200,height=330)


        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.sales_List=Listbox(sales_Frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_List.yview)
        self.sales_List.pack(fill=BOTH,expand=1)
        #self.sales_List.bind("<ButtonRelease-1>",self.get_data)

        #=======bill area==============
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=280,y=140,width=410,height=330)

        lbl_title2=Label(bill_Frame,text="Customer Bill Area",font=("goudy old style",20),bg="#4d636d",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X)


        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Listbox(bill_Frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

        #==========image=================================
        
        self.bill_photo=Image.open("images\store-img1.jpg")
        self.bill_photo=self.bill_photo.resize((350,350),Image.Resampling.LANCZOS )
 # type: ignore        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

        self.lbl_im1=Label(self.root,image=self.bill_photo,bd=2,relief=RAISED)
        self.lbl_im1.place(x=700,y=120)

        self.show()
    #===========================================================================================
    def show(self):
        self.sales_List.delete(0,END)
        print(os.listdir('bill'))
    for i in os.listdir('bill'):
        #print(i.split('.'),i.split('.')[-1])
        if i.split('.')[-1]=='txt':
            Self.sales_List.insert(END,i)
            
            

    '''def get_data(self,ev):
        index_=self.sales_List.curselection()
        file_name=self.sales_List.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()  '''  

if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()

   
