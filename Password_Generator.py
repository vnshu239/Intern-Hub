from tkinter import *
from random import randint

# Create main window
root = Tk()
root.title("Password Generator")
root.geometry("500x400")
root.config(bg="#f0f0f0")

# Generate a new random password
def new_rand():
    # Clear the password entry box
    pw_entry.delete(0, END)
    try:
        # Get password length from input
        pw_length = int(my_entry.get())
        my_password = "".join(chr(randint(33, 126)) for _ in range(pw_length))
        # Insert the generated password into the entry box
        pw_entry.insert(0, my_password)
    except ValueError:
        pw_entry.insert(0, "Invalid Input")
        
  

# Copy generated password to clipboard
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    root.update()

# Heading
header = Label(root, text="Password Generator", font=("Helvetica", 20, "bold"))
header.pack(pady=10)

# Labeled Border
length_frame = LabelFrame(root, text="Enter Password Length", font=("Helvetica", 12))
length_frame.pack(pady=10)

# Password Length
my_entry = Entry(length_frame, font=("Helvetica", 18), width=10, justify="center", relief=SOLID)
my_entry.pack(pady=10, padx=10)

# Password Output Box
pw_entry = Entry(root, font=("Helvetica", 18), justify="center", relief=SOLID, width=30)
pw_entry.pack(pady=20)

# Button Frame
btn_frame = Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=20)

# Button 1 -> Generate Password
generate_btn = Button(btn_frame, text="Generate Password", command=new_rand, font=("Helvetica", 12), bg="#4caf50", fg="white", relief=RAISED, padx=10)
generate_btn.grid(row=0, column=0, padx=20)

# Button 2 -> Copy to Clipboard
copy_btn = Button(btn_frame, text="Copy to Clipboard", command=clipper, font=("Helvetica", 12), bg="#2196f3", fg="white", relief=RAISED, padx=10)
copy_btn.grid(row=0, column=1, padx=20)

# Footer
footer = Label(root, text="Designed By Vansh", font=("Helvetica", 10), bg="#f0f0f0", fg="#777")
footer.pack(side=BOTTOM, pady=10)

root.mainloop()
