from tkinter import *
from OOPP import Database

with Database("books.db", "book") as database:
    def get_selected_row(event):
        global selTuple
        try:
            index = list1.curselection()[0]
            selTuple = list1.get(index)
        except :
            #messagebox.showinfo("Out of range", "Out of Range.")    
            pass
        e1.delete(0,END)
        e1.insert(END, selTuple[1])
        e2.delete(0,END)
        e2.insert(END, selTuple[2])
        e3.delete(0,END)
        e3.insert(END, selTuple[3])
        e4.delete(0,END)
        e4.insert(END, selTuple[4])

    def view_command():
        list1.delete(0, END)
        for row in database.view():
            list1.insert(END, row)

    def search_command():
        list1.delete(0, END)
        for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
            list1.insert(END, row)

    def add_command():
        if not (title_text.get == "" or author_text.get() == "" or year_text.get() == "" or isbn_text.get() == ""):
            list1.delete(0, END)
            database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
            view_command()    
        else:
            messagebox.showinfo("Wrong parameters entered", "You didn't enter values in all required fields.")    

    def delete_command():
        database.delete(selTuple[0])
        view_command()

    window = Tk()

    window.title("Bookstore")

    l1 = Label(window, text="Title")
    l1.grid(row=0, column=0)

    l2 = Label(window, text="Author")
    l2.grid(row=0, column=2)

    l3 = Label(window, text="Year")
    l3.grid(row=1, column=0)

    l4 = Label(window, text="ISBN")
    l4.grid(row=1, column=2)

    title_text = StringVar()
    e1 = Entry(window, textvariable=title_text)
    e1.grid(row=0, column=1)

    author_text = StringVar()
    e2 = Entry(window, textvariable=author_text)
    e2.grid(row=0, column=3)

    year_text = StringVar()
    e3 = Entry(window, textvariable=year_text)
    e3.grid(row=1, column=1)

    isbn_text = StringVar()
    e4 = Entry(window, textvariable=isbn_text)
    e4.grid(row=1, column=3)

    list1=Listbox(window, height=6, width=35)
    list1.selectbackground = 'blue'
    list1.grid(row=2, column=0, rowspan=6, columnspan=2)
    sb1=Scrollbar(window)
    sb1.grid(row=2, column=2, rowspan=6)
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>', get_selected_row)

    b1 = Button(window, text="View All", width=12, command=view_command)
    b1.grid(row=2, column=3)

    b2 = Button(window, text="Search entry", width=12, command=search_command)
    b2.grid(row=3, column=3)

    b3 = Button(window, text="Add entry", width=12, command=add_command)
    b3.grid(row=4, column=3)

    b4 = Button(window, text="Update selected", width=12)
    b4.grid(row=5, column=3)

    b5 = Button(window, text="Delete selected", width=12, command=delete_command)
    b5.grid(row=6, column=3)

    b6 = Button(window, text="Close", width=12, command=window.destroy)
    b6.grid(row=7, column=3)

    window.mainloop()
