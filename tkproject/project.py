import tkinter as tk
import os
import pymysql as mydb

screen = tk.Tk()
screen.title("Book Distribution Report")
screen.geometry("300x200")
screen.iconbitmap("books.png")

db = mydb.connect('localhost','root','ansh009@','tkinter')
cursor = db.cursor()


# This is the label of the app
label = tk.Label(screen,text='Today Book Distribution')
label.grid()

# This is the label for the first entry field
bookname = tk.Label(screen,text='Book Name : ')
bookname.grid(row=1,column=0)

# The first entry field
text = tk.Entry(screen)
text.grid(row=1,column=1)

# This is the label for the second field
qty = tk.Label(screen,text='Quantity')
qty.grid(row=2,column=0)

# This is the second entry field
qtyentry = tk.Entry(screen)
qtyentry.grid(row=2,column=1)

# This is the label for the third entry field.
area = tk.Label(screen,text='Area')
area.grid(row=3,column=0)

# This is the third entry field.
areaentry = tk.Entry(screen)
areaentry.grid(row=3,column=1)

name = text.get()
quantity = qtyentry.get()
area = areaentry.get()


def show():
    cursor.execute('INSERT INTO bookdistreport(book_name,qty,area) VALUES(%s,%s, %s)',(text.get(),qtyentry.get(),areaentry.get()))
    db.commit()
    db.close()
    print(qtyentry.get())
    screen.destroy()



submit = tk.Button(screen, text='Submit',bg='green',fg='white',command=show)
submit.grid(row=4,column=1)


screen.mainloop()
