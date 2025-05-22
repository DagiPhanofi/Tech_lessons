import tkinter as tk

# create an instance of a window
window = tk.Tk()

window.geometry("420x300")
window.title("Habesha Tech innovators first GUI")


label = tk.Label(window,text="Church login",font=("Georgia",16))
label.pack(pady = 12, padx=10)


entry1 = tk.Entry(window)
entry1.insert(0,'username')
entry1.pack(pady=12,padx=10)

entry2 = tk.Entry(window,show="*")
entry2.insert(0,'password')
entry2.pack(pady=12,padx=10)

def login_click():
    #print('Test!')
    print(entry1.get())
    if entry1.get()=='Dagmawi':
        label = tk.Label(window,text=("Welcome! "+ entry1.get()),font=("Georgia",12),fg="green")
        label.pack(pady = 12, padx=10)
    else:
        label = tk.Label(window,text="login failed!",font=("Georgia",12),fg="red")
        label.pack(pady = 12, padx=10)

button = tk.Button(window,text='Login',command=login_click)
button.pack(pady=12, padx=10)


checkbox = tk.Checkbutton(window,text='Remember Me')
checkbox.pack(pady= 12, padx=10)

# place window on the screen
window.mainloop()