import tkinter as tk
from tkinter import ttk

#Settings

#Fonts
FONT = "Courier New"
FONT_SIZE = 16
FONT_COLOR = "black"

#Window
TITLE = "Python Quizzer v1.0.0"
HEIGHT = 400
WIDTH = 800

WINDOW_BG = "black"

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



class App(tk.Tk):
    def __init__(self):

        # Initialize Window
        super().__init__()
        self.title(TITLE)
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.minsize(WIDTH,HEIGHT)
        self.configure(bg = WINDOW_BG)

        self.container = ttk.Frame(self, width = MAX_WIDTH, height = MAX_HEIGHT)
        self.container.pack()
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0,weight=1)

        self.container.pack_propagate(False)
        self.container.grid_propagate(False)


        #widgets
        self.set_style()
        self.title_menu = Title_Menu(self.container)
        
    
        # run mainloop
        self.mainloop()

    def set_style(self):
        style = ttk.Style()
        style.configure(
            "TFrame",
            background = WINDOW_BG
        )

        style.configure(
            "TButton", 
            background = "green", 
            foreground = FONT_COLOR,
            font = (FONT, FONT_SIZE)    
        )



class Title_Menu(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)


        self.build_widgets()
        self.build_layout()



        self.grid(row=0, column=0, sticky="nsew")



    def build_widgets(self):

        self.title = ttk.Label(
            self, foreground="#FFFF00", background="blue", 
            text = TITLE, font = (FONT, 36), anchor = "center"
        )

        self.frame = ttk.Frame(self)

        self.quiz = ttk.Button(
            self.frame, 
            text = "QUIZZES",
            command = lambda : None
        )
        self.settings = ttk.Button(
            self.frame, 
            text = "SETTINGS", 
            command = lambda : None
        )
        

    def build_layout(self):
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        self.title.pack(fill="x")
        self.frame.pack(fill="x")
        self.quiz.grid(row = 0, column = 0, sticky = "nsew", pady = 5)
        self.settings.grid(row = 0, column = 1, sticky = "nsew", pady = 5)










if __name__ == "__main__":
    App()