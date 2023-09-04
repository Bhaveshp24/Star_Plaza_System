from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class employeeClass:
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
        
        
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()

        #============searchFrame================
        SearchFrame=LabelFrame(self.root,text="search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="#352F44",fg="white")
        SearchFrame.place(x=250,y=20,width=650,height=70)

        #============Options================
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        text_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("ground old style",15),bg="white").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("ground old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=435,y=9,width=150,height=30)

        #===========title================
        title=Label(self.root,text="Employee Details",font=("goudyol style",15),bg="#4d636d",fg="white").place(x=50,y=100,width=1000)


        #===========Content=========================
        #======row1=================
        lbl_empid=Label(self.root,text="Emp ID",font=("goudyol style",15),bg="#352F44",fg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudyol style",15),bg="#352F44",fg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudyol style",15),bg="#352F44",fg="white").place(x=750,y=150)


        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudyol style",15),bg="white").place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudyol style",15),bg="white").place(x=850,y=150,width=180)


        #======row2=================
        lbl_name=Label(self.root,text="Name",font=("goudyol style",15),bg="#352F44",fg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudyol style",15),bg="#352F44",fg="white").place(x=350,y=190)
        lbl_doJ=Label(self.root,text="D.O.J",font=("goudyol style",15),bg="#352F44",fg="white").place(x=750,y=190)


        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudyol style",15),bg="white").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudyol style",15),bg="white").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudyol style",15),bg="white").place(x=850,y=190,width=180)


        #======row3=================
        lbl_email=Label(self.root,text="Email",font=("goudyol style",15),bg="#352F44",fg="white").place(x=50,y=230)
        lbl_password=Label(self.root,text="Password",font=("goudyol style",15),bg="#352F44",fg="white").place(x=750,y=230)  #place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudyol style",15),bg="#352F44",fg="white").place(x=350,y=230)    #place(x=750,y=230)


        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudyol style",15),bg="white").place(x=150,y=230,width=180)
        txt_password=Entry(self.root,textvariable=self.var_password,font=("goudyol style",15),bg="white").place(x=850,y=230,width=180)    #(x=500,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_utype.place(x=500,y=230,width=180)   #(x=850,y=230,width=180)
        cmb_utype.current(0)

        #======row4=================
        lbl_address=Label(self.root,text="Adress",font=("goudyol style",15),bg="#352F44",fg="white").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("goudyol style",15),bg="#352F44",fg="white").place(x=750,y=270)

        self.txt_address=Text(self.root,font=("goudyol style",15),bg="white")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudyol style",15),bg="white").place(x=850,y=270,width=180)


        #======button===========================
        btn_add=Button(self.root,text="Save",command=self.add,font=("ground old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Upadate",command=self.update,font=("ground old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.detele,font=("ground old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("ground old style",15),bg="#DBD8E3",fg="black",cursor="hand2").place(x=860,y=305,width=110,height=28)


        #===========Employee Details===================

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","password","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)  #tuples for data base name
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("password",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="salary")
        
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("password",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100) 
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#========================================================================================================================        

    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Mustbe required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID Already Assigned,Try Diffrent",parent=self.root)     
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,password,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                  
                                        self.var_emp_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),

                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        
                                        self.var_password.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Successful","Employee Added Sccessfully....",parent=self.root)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()                              #fetch the all records and show
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    
    
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        ROW=content['values']
        self.var_emp_id.set(ROW[0])
        self.var_name.set(ROW[1])
        self.var_email.set(ROW[2])
        self.var_gender.set(ROW[3])
        self.var_contact.set(ROW[4])


        self.var_dob.set(ROW[5])
        self.var_doj.set(ROW[6])
                                                
        self.var_password.set(ROW[7])
        self.var_utype.set(ROW[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,ROW[9])
        self.var_salary.set(ROW[10])
      
    
    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Mustbe required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)     
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,password=?,utype=?,address=?,salary=? where eid=?",(
                                  
                                        self.var_name.get(), 
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),

                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        
                                        self.var_password.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_salary.get(),
                                        self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Successful","Employee Updated Sccessfully....",parent=self.root)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def detele(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Mustbe required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)     
                else:
                    op=messagebox.askyesno("Confirm","do you really want to delete",parent=self.root)
                    if op==True:
                     cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                     con.commit()
                     messagebox.showinfo("Delete","Employee Deleted Sccessfully....",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")

        self.var_dob.set("")
        self.var_doj.set("")
                                                
        self.var_password.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                 messagebox.showerror("Error","Search input must be required",parent=self.root)
                
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()  
                if len(rows)!=0:                            #fetch the all records and show
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

if __name__=="__main__":

    root=Tk()
    obj=employeeClass(root)
    root.mainloop()