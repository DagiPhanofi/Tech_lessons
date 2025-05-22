#import all libraries you need 
import tkinter as tk

# create the window object
window = tk.Tk()

# now add a title to my window object 
window.title("Church Login")

# define the size of the window
window.geometry("420x300")

# create a label
my_header = tk.Label(window,text="Church login",font=("Georgia",16))

# now let us put this label on my window
my_header.pack(pady = 12, padx = 10)

# now add the entry for the username box
my_username_entry = tk.Entry(window)
my_username_entry.pack(pady = 12)
my_username_entry.insert(0,"username")

# now add the entry for the password 
my_password_entry = tk.Entry(window,show="*")
my_password_entry.pack(pady = 12)
my_password_entry.insert(0,"my password")










window.mainloop()
