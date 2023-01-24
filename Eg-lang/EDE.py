import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, "r") as file:
        text.insert("1.0", file.read())

def save_file():
    filepath = filedialog.asksaveasfilename()
    with open(filepath, "w") as file:
        file.write(text.get("1.0", "end"))

def save_as_file():
    filepath = filedialog.asksaveasfilename()
    with open(filepath, "w") as file:
        file.write(text.get("1.0", "end"))

root = tk.Tk()
root.config(bg='black')
text = tk.Text(root,bg='white')
# Create a label to display the line and column number
line_col_label = tk.Label(root)
line_col_label.pack(side='bottom')

# Function to update the line and column number display
def update_line_col_label(event):
    line_col = text.index(tk.INSERT).split('.')
    line_col_label.config(text="Line: {}   Column: {}".format(line_col[0], line_col[1]))

# Bind the function to the '<Motion>' event
text.bind('<Motion>', update_line_col_label)

# Create a tag for the word "PRINT"
text.tag_config("print", foreground="purple")

def check_for_print(event):
    current_line = text.get("insert linestart", "insert lineend")
    start_index = current_line.find("PRINT")
    if start_index != -1:
        end_index = start_index + len("PRINT")
        text.tag_add("print", "insert linestart + {} chars".format(start_index), "insert linestart + {} chars".format(end_index))
    else:
        text.tag_remove("print", "insert linestart", "insert lineend")

text.bind("<KeyRelease>", check_for_print)


text.pack(side='right', fill='both', expand=True)






menubar = tk.Menu(root)
file_menu = tk.Menu(menubar)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As...", command=save_as_file)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

root.mainloop()
