from tkinter import *
import tkinter.ttk
from tkinter import Tk, Frame, Menu

class Example(Frame):
    def __init__(self):
        super().__init__()   
        self.initUI()
        
    def initUI(self):
        self.master.title("Popup menu")
        self.menu = Menu(self.master, tearoff=0)
        self.menu.add_command(label="Beep", command=self.bell)
        self.menu.add_command(label="Exit", command=self.onExit)
        self.master.bind("<Button-3>", self.showMenu)
        self.pack()
        
    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    tree = tkinter.ttk.Treeview(root)
    tree["columns"]=("one","two")
    tree.column("one", width=100 )
    tree.column("two", width=100)
    tree.heading("one", text="coulmn A")
    tree.heading("two", text="column B")
    tree.insert("" , 0,    text="Line 1", values=("1A","1b"))
    id2 = tree.insert("", 1, "dir2", text="Dir 2")
    tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))
    ##alternatively:
    tree.insert("", 3, "dir3", text="Dir 3")
    tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))

    tree.pack()
    root.mainloop()  


if __name__ == '__main__':
    main()  




