#Notepad

from tkinter import * 
from tkinter import messagebox 
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import os 
import time 
 

# Functions for operations___>>>


# Function for new window
def closing_window(title):
    win = Tk()
    win.title("Notepad")

    # Some functions for this window...
    def to_close():
        win.destroy()
    
    def dont_save():
        global file
        root.title('*Untitled - Notepad')
        file = None
        textArea.delete(1.0,END)
        win.destroy()
        print("New Window Opened...")
    
    def save_file():
        saveFile()
        # win.destroy()
        print("Win Destroyed...")
        dont_save()



    Label(win, text=f'  Do you want to save changes to {title}? ', font='Lucida 16').pack(pady=18)

    new_frame = Frame(win)
    new_frame.pack(side=BOTTOM, fill=X, pady=5)
    Button(new_frame, text="  Close  ", command=to_close).pack(side=RIGHT,fill=X, padx=5)
    Button(new_frame, text="  Don't Save  ", command=dont_save).pack(side=RIGHT,fill=X, padx=5)
    Button(new_frame, text="  Save  ", command=save_file).pack(side=RIGHT,fill=X, padx=5)

    win.mainloop()
    return



# Filemenu Functions
def newFile():
    global file
    text = textArea.get(1.0,END)
    title = root.title()[:-10]
    if len(text) <= 1:
        root.title('*Untitled - Notepad')
        file = None 
        textArea.delete(1.0,END)
        print("New File Opened...")
    else:
        print("Closing_Window Opened...")
        closing_window(title=title)

 
def openFile():
    global file
    file = askopenfilename(defaultextension='*.txt', filetypes=[("All Files","*.*"), 
                                                                ("Text Documents", "*.txt")]) 
    
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0,END)
        with open(file, 'r') as f:
            textArea.insert(1.0,f.read())
    print("File Opened...")
 

def saveFile():
    try:
        global file
        with open(file, "w") as f:
            f.write(textArea.get(1.0,END))
            print("File Saved...")
    except Exception as e:
        saveasFile()


def saveasFile():
    global file
    file = asksaveasfilename(initialfile='*.txt', defaultextension='*.txt', filetypes=[("All Files","*.*"), 
                                                                ("Text Documents", "*.txt")])
      
    try:
        with open(file, "w") as f:
            f.write(textArea.get(1.0,END))
        root.title(os.path.basename(file) +" - Notepad")
        print("File Saved as...")
    except Exception as e:
        return

def close():
    text = textArea.get(1.0,END)
    if len(text) <= 1:
        root.destroy()
    else:
        choice = messagebox.askquestion('Notepad', 'Do you want to quit?')
        if choice == 'Yes' or choice == 'yes':
            textArea.delete(1.0,END)
        else:
            return
             
 
# Editmenu Functions
def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def delete():
    textArea.event_generate("<<Clear>>")

def select_all():
    textArea.event_generate("<<SelectAll>>")

def clear_all():
    choice = messagebox.askquestion('Notepad', 'Do you want to clear all the text?')
    if choice == 'Yes' or choice == 'yes':
        textArea.delete(1.0,END)
    else:
        return

def time_date():
    hr = time.strftime('%H')
    if int(hr) > 12:
        hr = int(int(hr)-12)
    yr = 20
    date_and_time = time.strftime(f'{hr}:%M %p - %a %d/%m/{yr}%y')
    textArea.insert(END, date_and_time)



# Formatmenu Functions
def zoom_in():
    global font_size, zooming_ratio
    font_size += 2
    zooming_ratio += 10
    zooming.config(text=f"|   {zooming_ratio}%   ")
    textArea.config(font=f'Consolas {font_size}')

def zoom_out():
    global font_size, zooming_ratio
    font_size -= 2
    zooming_ratio -= 10
    zooming.config(text=f"|   {zooming_ratio}%   ")
    textArea.config(font=f'Consolas {font_size}')

# Helpmenu Functions
def about_notepad():
    messagebox.showinfo('About', 'Notepad by Hassan Khan.')


# Status Bar Functions >>>
# Default size and zoom ratio
font_size = 11
zooming_ratio = 100

# appearance Modes
def light_mode():
    textArea.config(bg='white', fg='black')
    menuBar.config(bg='white', fg='black')
    fileMenu.config(bg='white', fg='black')
    editMenu.config(bg='white', fg='black')
    formatMenu.config(bg='white', fg='black')
    helpMenu.config(bg='white', fg='black')

def dark_mode():
    textArea.config(bg='black', fg='white')
    menuBar.config(bg='black', fg='white')
    fileMenu.config(bg='black', fg='white')
    editMenu.config(bg='black', fg='white')
    formatMenu.config(bg='black', fg='white')
    helpMenu.config(bg='black', fg='white')

# GUI Script___>>>
if __name__ == '__main__':

    root = Tk()
    root.title('Untitled - Notepad')
    root.geometry("525x420")
    image_icon = PhotoImage(file='logo.png')
    root.iconphoto(False, image_icon)


    # Text Area
    file = None

    textvar = StringVar()
    textArea = Text(root, bg='white', fg='black',font=f'Consolas {font_size}')
    textArea.pack(expand=True, fill=BOTH)

    # StatusBar
    statusBar = Frame(root).pack(side=BOTTOM, fill=X, pady=2)
    status_bar_label = Label(statusBar, text="|  Status Bar").pack(side=LEFT,fill=X, padx=5)
    zooming = Label(statusBar, text=f"|  {zooming_ratio}%")
    zooming.pack(side=LEFT,fill=X, padx=5)
    appearance_label = Label(statusBar, text="|  Appearance -->").pack(side=LEFT,fill=X, padx=5)

    var = IntVar()
    Radiobutton(statusBar, variable=var, value=0,text="Light Mode", command=light_mode).pack(side=LEFT,fill=X, padx=3)
    Radiobutton(statusBar, variable=var, value=1, text="Dark Mode",command=dark_mode).pack(side=LEFT,fill=X, padx=3)

    # Menu Bar
    menuBar = Menu(root,bg='black', fg='white')

    # ScrollBar
    scrollBar = Scrollbar(textArea)
    scrollBar.pack(side=RIGHT, fill=Y)
    scrollBar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)


    # File SubmenuBar
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_command(label="Save As...", command=saveasFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=close)
    # Adding to main MenuBar
    menuBar.add_cascade(label="File", menu=fileMenu)


    # Edit SubmenuBar
    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    editMenu.add_command(label="Delete", command=delete)
    editMenu.add_separator()
    editMenu.add_command(label="Select All", command=select_all)
    editMenu.add_command(label="Clear All", command=clear_all)
    editMenu.add_command(label="Time/Date", command=time_date)
    # Adding to main MenuBar
    menuBar.add_cascade(label="Edit", menu=editMenu)

    # Foramt SubmenuBar
    formatMenu = Menu(menuBar, tearoff=0)
    formatMenu.add_command(label="Zoom In", command=zoom_in)
    formatMenu.add_command(label="Zoom Out", command=zoom_out)
    formatMenu.add_separator()

    # Adding to main MenuBar
    menuBar.add_cascade(label="Format", menu=formatMenu)


    # Help SubmenuBar
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=about_notepad)
    # Adding to main MenuBar
    menuBar.add_cascade(label="Help", menu=helpMenu)

    # Configuring menuBar with root  >>>
    root.config(menu=menuBar)

    # Running program
    root.mainloop()