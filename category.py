from tkinter import*
from tkinter.tix import ROW
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | created by Bhavesh Patil")
        self.root.config(bg="#352F44")
        self.root.focus_force() 


        #====variable===================
        self.var_cat_id=StringVar()
        self.var_name=StringVar()


        #========title==============
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#4d636d",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="#352F44",fg="white").place(x=50,y=100)
        lbl_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="white").place(x=50,y=170,width=300)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",command=self.detele,font=("goudy old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=520,y=170,width=150,height=30)


        #=====category Details===================================
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category_Table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)  #tuples for data base name
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_Table.xview)
        scrolly.config(command=self.category_Table.yview)
        self.category_Table.heading("cid",text="C ID")
        self.category_Table.heading("name",text="Name")
        self.category_Table["show"]="headings"
        self.category_Table.column("cid",width=90)
        self.category_Table.column("name",width=100)
        self.category_Table.pack(fill=BOTH,expand=1)
        self.category_Table.bind("<ButtonRelease-1>",self.get_data)


        #======images=========
        self.im1=Image.open("images\store-img1.jpg")
        self.im1=self.im1.resize((500,250),Image.Resampling.LANCZOS )
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)

        self.im2=Image.open("images\supermarket.jpg")
        self.im2=self.im2.resize((500,250),Image.Resampling.LANCZOS )
        self.im2=ImageTk.PhotoImage(self.im2)

        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)

        self.show()


    #==============================functions============================================================

    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category name shuld  be required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category Already present,Try Diffrent",parent=self.root)     
                else:
                    cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Successful","Category Added Sccessfully....",parent=self.root)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()                         #fetch the all records and show
            self.category_Table.delete(*self.category_Table.get_children())
            for row in rows:
                self.category_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    
    


    def get_data(self,ev):
        f=self.category_Table.focus()
        content=(self.category_Table.item(f))
        ROW=content['values']
        #print(ROW)
        self.var_cat_id.set(ROW[0])
        self.var_name.set(ROW[1])


    def detele(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","please selet or category from the list",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error, please try again.",parent=self.root)     
                else:
                    op=messagebox.askyesno("Confirm","do you really want to delete",parent=self.root)
                    if op==True:
                     cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                     con.commit()
                     messagebox.showinfo("Delete","Category Deleted Sccessfully....",parent=self.root)
                    self.show()
                    self.var_cat_id.set("")
                    self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

   
if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()
