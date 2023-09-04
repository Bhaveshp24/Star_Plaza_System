import tkinter as TK
import tkinter
from webbrowser import BackgroundBrowser 

class Home:
    def about(self,root):           #default constrctor
        self.root=root
        self.root.geometry("1360x700+0+0")
        self.root.title("ShopyApp")
        self.root.config(bg="white")
        
 
        #=======MENU============================
        
        menubare=TK.Menu(self.root,background='#ff8000',foreground='black',activeforeground='black')
        file=TK.Menu(menubare,tearoff=1,background='#ffcc99',foreground='black')
        file.add_command(label="new")
        file.add_command(label="open")
        file.add_command(label="save")
        file.add_command(label="save as")
        file.add_separator()
        file.add_command(label="exit",command=root.quit)
        
        menubare.add_cascade(label='File',menu=file)
        edit=TK.Menu(menubare,tearoff=0)
        edit.add_cascade(label='Undo')
        edit.add_separator()
        edit.add_cascade(label='Cut',)
        
        edit.add_cascade(label='Copy',)
        
        menubare.add_cascade(label='Paste',menu=edit)
        help=TK.Menu(menubare,tearoff=0)
        help.add_command(label="About",command=root.about)
        menubare.add_cascade(label="Help",menu=help)
        root.config(menu=menubare)
        root.mainloop()
        
    '''     
if __name__=="__main__":
    root= TK.Tk()

    object=Home(root)
    root.mainloop()'''