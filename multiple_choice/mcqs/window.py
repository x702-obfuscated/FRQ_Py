from pathlib import Path
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

#Paths
FILEPATH = Path(__file__).parent
IMGPATH = FILEPATH / "img" 

#Fonts
FONT = "Courier New"
FONT_SIZE = 16
FONT_COLOR = "#d9d9d9"

#Window
TITLE = "Python Quiz Taker v1.0.0"
HEIGHT = 400
WIDTH = 800

WINDOW_BG = "#242424"

# Quiz Name Label
QUIZ_NAME = "PLACEHOLDER QUIZ NAME"

#Question Number Label
LABEL_BG = "#75f56e"

# Text Prompt
PROMPT_BG = "#d1c18a"

# Buttons
BUTTON_BG = PROMPT_BG
BUTTON_HIGHLIGHT = "#75f56e"

MAX_HEIGHT = 1080
MAX_WIDTH =  940 #window.winfo_screenwidth()/2
MAX_CHARS = 86

def show_frame(frame):
    frame.tkraise()

# Function to change the background color on hover
def on_enter(event):
    event.widget.config(bg=BUTTON_HIGHLIGHT)  # Change background color on hover

# Function to revert the background color when the mouse leaves
def on_leave(event):
    event.widget.config(bg=BUTTON_BG)  # Reset to default button color


def main() -> None:
    # Create the main application window
    window.title(TITLE)
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.minsize(500,500)
    window.configure(bg = WINDOW_BG)


    # icon = tk.PhotoImage(file= IMGPATH / "python_logo.png")  
    # window.iconphoto(False, icon)  

    # Main container for frames
    container = tk.Frame(window, width=MAX_WIDTH, height=MAX_HEIGHT)
    container.pack()
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0,weight=1)

    container.pack_propagate(False)
    container.grid_propagate(False)


    #FRAMES
    frames = []

    main_view = tk.Frame(container, bg=WINDOW_BG)
    quiz_menu_view = tk.Frame(container, bg = WINDOW_BG)
    quiz_view = tk.Frame(container,bd=5, relief="raised", pady=5, bg=WINDOW_BG)
    settings_view = tk.Frame(container,bg=WINDOW_BG )

    frames.append(main_view)
    frames.append(quiz_menu_view)
    frames.append(quiz_view)
    frames.append(settings_view)

    for frame in frames:
        frame.grid(row=0, column=0, sticky="nsew")

    show_frame(main_view)

    # MAIN_VIEW
    title_label = tk.Label(main_view,fg="yellow", bg="blue", text=TITLE, font= (FONT, 36))
    main_menu = tk.Frame(main_view, bg=WINDOW_BG, bd = 5, relief = "raised")
    quiz_menu_button = tk.Button(main_menu,activebackground=BUTTON_HIGHLIGHT, text="QUIZZES", font=(FONT, 14), bg=BUTTON_BG, command= lambda: show_frame(quiz_view))
    settings_menu_button = tk.Button(main_menu, activebackground=BUTTON_HIGHLIGHT, text="SETTINGS", font=(FONT, 14), bg=BUTTON_BG, command= lambda: show_frame(settings_view))

    main_menu.grid_columnconfigure(0, weight=1)
    main_menu.grid_columnconfigure(1, weight=1)
    
    title_label.pack(fill="x")
    main_menu.pack(fill="x")
    quiz_menu_button.grid(row = 0, column = 0, sticky = "nsew")
    settings_menu_button.grid(row = 0, column = 1, sticky = "nsew")

    quiz_menu_button.bind("<Enter>", on_enter)
    quiz_menu_button.bind("<Leave>", on_leave)


    settings_menu_button.bind("<Enter>", on_enter)
    settings_menu_button.bind("<Leave>", on_leave)

    
  




    # QUIZ_MENU_VIEW



    window.mainloop()


main()


















# main_title = tk.Label(main_view,text=TITLE, font=(FONT, 48), bg=LABEL_BG)




# quiz_view.pack_propagate(False)





# # Function to change the background color on hover
# def on_enter(event):
#     event.widget.config(bg=BUTTON_HIGHLIGHT)  # Change background color on hover

# # Function to revert the background color when the mouse leaves
# def on_leave(event):
#     event.widget.config(bg=BUTTON_BG)  # Reset to default button color


# # Function that gets called when a button is clicked
# def on_choice_click(choice):
#     # messagebox.showinfo("Your Choice", f"You selected: {choice}")
#     next_question()

# def on_window_close():
#     if messagebox.askokcancel("Exit", "Are you sure that you want to quit?"):
#         window.destroy()  # Closes the window

# # Bind the window close event to the custom function
# window.protocol("WM_DELETE_WINDOW", on_window_close)


# labels = []

# label_frame = tk.Frame(quiz_view,  bd=5, relief="raised", pady=5, bg=WINDOW_BG)
# label_frame.pack(fill="x")
# # label_frame.grid_propagate(False)

# # Add a text box for the question number (read-only)
# n = 1
# q_num = tk.Label(label_frame, height=1, width=15, font=(FONT, 16), bg=LABEL_BG)
# q_num.config(text=f"Question {n}")
# # q_num.pack(side="left",anchor="nw", )
# q_num.grid(row=0, column=0, sticky="nsew")
# labels.append(q_num)

# quiz_label = tk.Label(label_frame, height=1, font=(FONT, 16), bg=LABEL_BG)
# quiz_label.config(text=QUIZ_NAME)
# # quiz_label.pack(side="left", padx= 5)
# quiz_label.grid( row=0, column=1,sticky="nsew", padx=5)
# labels.append(quiz_label)


# correct = 5
# total = 10
# correct_label = tk.Label(label_frame, height=1, font=(FONT, 16), bg=LABEL_BG)
# correct_label.config(text=f"{correct} out of {total}: {round(correct / total * 100)}%")
# # correct_label.pack(side="left")
# correct_label.grid(row=0, column=2, sticky="nsew")
# labels.append(correct_label)


# for i in range(len(labels)):
#     label_frame.grid_columnconfigure(i, weight = 1)




# # Add a text box for the Python question prompt (read-only)
# question_text = tk.Text(quiz_view, height=6, width=MAX_CHARS, font=(FONT, 14))
# question = (
#     "What is the output of the following Python code?\n\n"
#     "for i in range(1, 6):\n"
#     "    print(i)\n"
# )
# question_text.insert(tk.END, question)
# question_text.config(state="disabled", bg=PROMPT_BG)  
# question_text.pack( pady=5)

# # Create a frame for the answer buttons
# button_frame = tk.Frame(quiz_view,bd=5,relief="ridge", bg=WINDOW_BG)
# button_frame.pack(fill="x")
# # button_frame.pack_propagate(False)





# # button_frame.columnconfigure([0, 1], weight=1, uniform="equal")
# # button_frame.rowconfigure([0, 1], weight=1, uniform="equal")

# # Create the buttons for choices and place them in the center in a 2x2 grid
# choices = ["1 2 3 4 5", "0 1 2 3 4", "1 2 3 4", "Error"]

# # Button positions in a 2x2 grid
# # button1 = tk.Button(button_frame, text=choices[0], font=("Arial", 14), command=lambda: on_choice_click(choices[0]))
# # button1.grid(row=0, column=0,  sticky="nsew", ipadx=5, ipady=5)

# # button2 = tk.Button(button_frame, text=choices[1], font=("Arial", 14), command=lambda: on_choice_click(choices[1]))
# # button2.grid(row=0, column=1, sticky="nsew", ipadx=5, ipady=5)

# # button3 = tk.Button(button_frame, text=choices[2], font=("Arial", 14), command=lambda: on_choice_click(choices[2]))
# # button3.grid(row=1, column=0, sticky="nsew", ipadx=5, ipady=5)

# # button4 = tk.Button(button_frame, text=choices[3], font=("Arial", 14), command=lambda: on_choice_click(choices[3]))
# # button4.grid(row=1, column=1, sticky="nsew", ipadx=5, ipady=5)


# choice_buttons = []
# for choice in choices:
#     button = tk.Button(button_frame,activebackground=BUTTON_HIGHLIGHT, text=choice, font=(FONT, 14), bg=BUTTON_BG, command=lambda c=choice: on_choice_click(c))
#     button.pack(fill = "x", pady = 5)
#     # button.bind("<Enter>", on_enter)
#     # button.bind("<Leave>", on_leave)
#     choice_buttons.append(button)




# # Function to update the question and choices
# def update_question(question_text_value, new_choices):
#     # Update the question text
#     question_text.config(state="normal")  # Make the text widget editable
#     question_text.delete(1.0, tk.END)  # Clear the current text
#     question_text.insert(tk.END, question_text_value)  # Insert the new question
#     question_text.config(state="disabled")  # Make it read-only again

#     # Update the answer buttons

#     for i,choice in enumerate(new_choices):
#         choice_buttons[i].config(text=choice, command=lambda: on_choice_click(choice))


# # Example of updating the question and answers
# def next_question():
#     new_question = (
#         "What will be printed by the following code?\n\n"
#         "for i in range(2, 10, 2):\n"
#         "    print(i)\n"
#     )
#     new_choices = ["2 4 6 8", "2 4 6 8 10", "Error", "None of the above"]
#     update_question(new_question, new_choices)
#     q_num.config(text = f"Question {n + 1}")
#     q_num.grid(row=0, column=0, sticky="nsew")

# # Add a button to load the next question
# # next_button = tk.Button(window, text="Next Question", font=("Arial", 14), command=next_question)
# # next_button.pack(pady=20)




# #Menu
# menu_buttons = []
# menu_frame = tk.Frame(quiz_view,  pady=5, bg=WINDOW_BG)
# menu_frame.pack(fill="x")
# # menu_frame.grid_propagate(False)

# restart_button = tk.Button(menu_frame, activebackground=BUTTON_HIGHLIGHT, text="RESTART", font=(FONT, 14), bg=BUTTON_BG, command=lambda: None)
# settings_button = tk.Button(menu_frame, activebackground=BUTTON_HIGHLIGHT, text="SETTINGS", font=(FONT, 14), bg=BUTTON_BG, command=lambda: None)

# # restart_button.bind("<Enter>", on_enter)
# # restart_button.bind("<Leave>", on_leave)

# # settings_button.bind("<Enter>", on_enter)
# # settings_button.bind("<Leave>", on_leave)

# menu_buttons.append(restart_button)
# menu_buttons.append(settings_button)

# for i,e in enumerate(menu_buttons):
#     e.grid(row=0, column= i, sticky="nsew")
#     menu_frame.grid_columnconfigure(i, weight = 1)



# # Start the Tkinter event loop
# window.mainloop()