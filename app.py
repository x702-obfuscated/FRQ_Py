import os,sys
from pathlib import Path
import shutil
import subprocess

home = Path.home() / "Desktop"
cspath = home / "INTRO-TO-COMP-SCI"



import tkinter as tk

# Sample dependent options
options_map = {
    "1-Comments-Data-Variables-Operators": [
        "1-Comments-Input-Output-Erros",
        "2-Syntax",
        "3-Data",
        "4-Variables",
        "5-Operators",
        "6-Simple-Functions-and-Calls",
        "7-Strings"
    ],
    "2-Collections": [
        "21-Lists",
        "22-Tuples",
        "23-Sets",
        "24-Dictionaries"
    ],
    "3-Conditionals": [
        "31-Boolean-Expressions",
        "32-Conditionals"
    ],
    "4-Iteration": [
        "41-While-Loops",
        "42-For-Loops",
        "43-Iterate1DCollections",
        "44-Iterate2DCollections",
        "45-Iterators",
        "46-Generatots"
    ],
    "5-Functions": [
        "51-Functions",
        "52-Recursion",
        "53-Lambdas",
        "54-Decorators"
    ],
    "6-Objects-and-Classes": [
        "61-Classes",
        "62-Objects",
        "63-Methods",
        "64-Inheritence",
        "65-Modules"
    ]
}

def update_second_dropdown(*args):
    category = category_var.get()

   
    items = options_map.get(category, [None])
    
    # Clear existing menu items
    menu = item_dropdown["menu"]
    menu.delete(0, "end")

    # Add new menu items
    for item in items:
        menu.add_command(label=item, command=lambda value=item: item_var.set(value))

    # Set default value
    if items:
        item_var.set(items[0])
    else:
        item_var.set("")


def setup(name):
    if name == "None":
        return
    path = cspath / name
    try:
        if not os.path.exists(cspath):
            os.mkdir(cspath)

        if not os.path.exists(path):
            os.mkdir(path)


            open(path / "main.py","x").close()
            open(path / "test.py","x").close()

        if shutil.which("code"):
            subprocess.run([shutil.which("code"), path])
        elif shutil.which("explorer"):
            subprocess.run([shutil.which("explorer"),path])


    except Exception as e:
        print(path)
        print(e)
        sys.exit()

def on_submit():
    setup(item_var.get())


root = tk.Tk()
root.title("FRQ_Py")
root.geometry("300x150")
root.resizable(False,False)
root.config(bg="#0339fc")

frame = tk.Frame(root, bg="#0339fc")
frame.place(relx=0, rely=0.5, relwidth=1.0, anchor="w")

# First dropdown (category)
category_var = tk.StringVar(frame)
category_var.set("PICK A CHAPTER")  # Default
category_dropdown = tk.OptionMenu(frame, category_var, *options_map.keys())
category_dropdown.config(width=40)
category_dropdown.pack(pady=10)

# Second dropdown (items)
item_var = tk.StringVar(frame)
item_dropdown = tk.OptionMenu(frame, item_var, "")
item_dropdown.config(width=40)
item_dropdown.pack(pady=10)

# Update items on category change
category_var.trace_add("write", update_second_dropdown)
update_second_dropdown()  # Initialize

# Submit button
submit_button = tk.Button(frame, text="Submit", command=on_submit)
submit_button.config(width=35)
submit_button.pack(pady=10)



root.mainloop()




