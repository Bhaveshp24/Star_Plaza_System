from tkinter import *
import _multiprocessing as mp
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
#from sales import salesClass
class IMS:
    def __init__(self,root):           #default constrctor
        self.root=root
        self.root.geometry("1359x700+0+0")
        self.root.title("Inventory Management System | created by Mr. Bhavesh Patil and Ms.Aarti Patil")
        self.root.config(bg="#352F44")

        #===============title img===============
        #self.icon_title=PhotoImage(file="images\topcircle.jpg")
        #self.img_title=Image.open("images\AdobeStock.jpg")
        #self.img_title=self.img_title.resize((50,50))
        #self.img_title=ImageTk.PhotoImage(self.img_title)
        
        

        #lbl_img_title=Label(image=self.img_title)
        #lbl_img_title.pack(side=TOP,fill=X)

        #===============title===============
        #title=Label(self.root,text="Star Plaza Storage System",image=self.img_title,compound=LEFT,font=("tome new roman",40,"bold"),bg="#2A2438",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        

        #=======button_logout======================
        #btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="#DBD8E3",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        '''#=======clock======================
        self.lbl_clock=Label(self.root,text="Welcome To Inventory System\t\t Date: DD-MM-YYYY\t\t Time: HH-MM-SS",font=("tome new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)'''


         #=======Left Menu======================
        #self.MenuLogo=Image.open("images\AdobeStock.jpg")
        #self.MenuLogo=self.MenuLogo.resize((200,200))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="#5C5470")
        LeftMenu.place(x=0,y=102,width=200,height=570)

        lbl_MenuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_MenuLogo.pack(side=TOP,fill=X)

    
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20,"bold"),bg="#B0B3D6").pack(side=TOP,fill=X)
        
        btn_Employee=Button(LeftMenu,text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="#DBD8E3",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Supplyer=Button(LeftMenu,text="Supplyer",command=self.supplier,font=("times new roman",20,"bold"),bg="#DBD8E3",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Category=Button(LeftMenu,text="Category",command=self.category,font=("times new roman",20,"bold"),bg="#DBD8E3",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Product=Button(LeftMenu,text="Product",command=self.product,font=("times new roman",20,"bold"),bg="#DBD8E3",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        #btn_Sales=Button(LeftMenu,text="Sales",command=self.sales,font=("times new roman",20,"bold"),bg="#DBD8E3",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Exit=Button(LeftMenu,text="Exit",font=("times new roman",20,"bold"),bg="#DBD8E3",bd=3,cursor="hand2").pack(side=TOP,fill=X)



         #=======Content======================
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ] ",bd=5,relief=RIDGE,bg="#A7D9C9",fg="white",font=("italic",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_Supplyer=Label(self.root,text="Total Supplyer\n[ 0 ] ",bd=5,relief=RIDGE,bg="#BF7781",fg="white",font=("italic",20,"bold"))
        self.lbl_Supplyer.place(x=650,y=120,height=150,width=300)

        self.lbl_Category=Label(self.root,text="Total Category\n[ 0 ] ",bd=5,relief=RIDGE,bg="#93c47d",fg="white",font=("italic",20,"bold"))
        self.lbl_Category.place(x=1000,y=120,height=150,width=300)

        self.lbl_Product=Label(self.root,text="Total Product\n[ 0 ] ",bd=5,relief=RIDGE,bg="#f9cb9c",fg="white",font=("italic",20,"bold"))
        self.lbl_Product.place(x=300,y=300,height=150,width=300)

        self.lbl_Sales=Label(self.root,text="Total Sales\n[ 0 ] ",bd=5,relief=RIDGE,bg="#ffbdd2",fg="white",font=("italic",20,"bold"))
        self.lbl_Sales.place(x=650,y=300,height=150,width=300)



         #=======footer======================
        lbl_footer=Label(self.root,text="IMS Inventory Management System\n | Developed By Bhavesh Patil & Shreyash Shinde",font=("tome new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)



#=================================================================================================================
    
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

''' def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)'''

if __name__=="__main__":
   
    root=Tk()
    obj=IMS(root)
    root.mainloop()