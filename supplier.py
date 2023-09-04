from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | created by Bhavesh Patil")
        self.root.config(bg="#352F44")
        self.root.focus_force()       
        #===================================
        # All variables================

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        self.var_sup_invoice=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
       

        #============searchFrame================
        #============Options================
        lbl_search=Label(self.root,text="Invoice No.",bg="#352F44",fg="white",font=("goudy old style",15))
        lbl_search.place(x=700,y=80)
        

        text_search=Entry(self.root,textvariable=self.var_searchtxt,font=("ground old style",15),bg="white").place(x=800,y=80,width=160)
        btn_search=Button(self.root,text="Search",command=self.search,font=("ground old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=980,y=80,width=100,height=28)

        #===========title================
        titl=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#4d636d",fg="white").place(x=50,y=10,width=1000,height=40)


        #===========Content=========================
        #======row1=================
        lbl_suplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="#352F44",fg="white").place(x=50,y=80)
        txt_suplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="white").place(x=180,y=80,width=180)
        

        #======row2=================
        lbl_name=Label(self.root,text="Name",font=("goudyol style",15),bg="#352F44",fg="white").place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="white").place(x=180,y=120,width=180)

        #======row3=================
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="#352F44",fg="white").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="white").place(x=180,y=160,width=180)
       
        #======row4=================
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="#352F44",fg="white").place(x=50,y=200)
        self.var_desc=Text(self.root,font=("goudyol style",15),bg="white")
        self.var_desc.place(x=180,y=200,width=470,height=120)
       

        #======button===========================
        btn_add=Button(self.root,text="Save",command=self.add,font=("ground old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Upadate",command=self.update,font=("ground old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.detele,font=("ground old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("ground old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=540,y=370,width=110,height=35)


        #===========Employee Details===================

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)  #tuples for data base name
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")
        
        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#========================================================================================================================        

    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice ID Mustbe required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice no. Already Assigned,Try Diffrent",parent=self.root)     
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                  
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.var_desc.get('1.0',END),
                                       
                    ))
                    con.commit()
                    messagebox.showinfo("Successful","Supplier Added Sccessfully....",parent=self.root)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()                              #fetch the all records and show
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    
    

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        ROW=content['values']
        #print(ROW)
        self.var_sup_invoice.set(ROW[0])
        self.var_name.set(ROW[1])
        self.var_contact.set(ROW[2])
        self.var_desc.delete('1.0',END)
        self.var_desc.insert(END,ROW[3])
            
    
    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. Must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)     
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                  
                                        self.var_name.get(), 
                                        self.var_contact.get(),
                                        self.var_desc.get('1.0',END),
                                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Successful","Supplier Updated Sccessfully....",parent=self.root)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def detele(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. Must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)     
                else:
                    op=messagebox.askyesno("Confirm","do you really want to delete",parent=self.root)
                    if op==True:
                     cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                     con.commit()
                     messagebox.showinfo("Delete","suppliere Deleted Sccessfully....",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                 messagebox.showerror("Error","Invoice no must be required",parent=self.root)    
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()  
                if row!=None:                            #fetch the all records and show
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()
