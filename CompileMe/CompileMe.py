# Import the tkinter module to create a GUI (Graphical User Interface).
from tkinter import *
import sys
import os
import webbrowser
import tkinter as tk
# Import specific functions from the tkinter library for file dialog and message box.
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
# Import the tkinter module with an alias 'tk' for convenience.

# Import custom modules syntax.py and lexical.py for additional functionality.
import syntax as sy
import lexical as lx

# Define global variables to be used across functions or parts of the program.
global input_text1  # Placeholder for a Tkinter text widget or related input field.
global input_text2  # Placeholder for another Tkinter text widget or related input field.
global input_text3  # Placeholder for yet another Tkinter text widget or related input field.
global filename  # Placeholder for storing the name of the current file.
global root


# These global variables may be utilized to store and access information across different parts of the program.
def main():
    global input_text1
    global input_text2
    global input_text3

    # Parent window declaration and configuration
    w = 780
    h = 745
    global root
    root = Tk()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2) - 35
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root.title("CompileMe")

    mainLabelColor = "#E16428"
    backgroundColor = "#3C3F41"
    textBackgroundColor = "#2B2B2B"
    textColor = "#F6E9E9"
    buttonBackgroundColor = "#272727"
    buttonColor = "#E79A58"
    labelColor = "#EEEEEE"

    root.configure(background=backgroundColor)
    root.resizable(0, 0)

    # Labels
    Label(root, text="CompileMe", font=("Arial", 25), bg=backgroundColor, fg=mainLabelColor).place(x=300, y=20)
    Label(root, text="Lexical and Syntax Analyzer(PYTHON)", font=("Arial", 10), bg=backgroundColor,
          fg=labelColor).place(x=470, y=36)
    Label(root, text="The translated program was saved in the file \"graph.txt\". \nYou can view the content of the "
                     "file at www.webgraphviz.com", font=("Arial", 10), bg=backgroundColor, fg=labelColor).place(x=200,
                                                                                                                 y=700)
    Label(root, text="SOURCE CODE", bg=backgroundColor, fg=labelColor).place(x=20, y=130)
    Label(root, text="LEXICAL ANALYSIS", bg=backgroundColor, fg=labelColor).place(x=20, y=375)
    Label(root, text="SYNTAX ANALYSIS", bg=backgroundColor, fg=labelColor).place(x=400, y=375)
    # Buttons
    Button(root, text="Import file (.py)", font=("Arial", 10, "bold"), bg=buttonBackgroundColor,
           cursor="hand2", fg=buttonColor, padx=8, pady=5, command=lookForFile).place(x=20, y=90)
    Button(root, text="Delete", pady=5, font=("Arial", 10, "bold"), cursor="hand2",
           bg="#952323", fg="#EEEEEE", command=eraseCode).place(x=708, y=298)
    Button(root, text="Restart", font=("Arial", 10, "bold"), cursor="hand2",
           bg="#952323", fg="#EEEEEE", command=restart_application).place(x=708, y=705)
    Button(root, text="visualize", font=("Arial", 10, "bold"), cursor="hand2",
           bg=buttonBackgroundColor, fg=buttonColor, command=visual).place(x=633, y=705)
    Button(root, text="Lexical analysis", font=("Arial", 10, "bold"), bg=buttonBackgroundColor,
           cursor="hand2", padx=8, pady=5, fg=buttonColor, command=executeLexical).place(x=20, y=337)

    Button(root, text="Syntax Analysis", font=("Arial", 10, "bold"), bg=buttonBackgroundColor,
           cursor="hand2", padx=8, pady=5, fg=buttonColor, command=executeSyntax).place(x=400, y=337)
    Button(root, text="Prepare Code", font=("Arial", 10, "bold"), bg=buttonBackgroundColor,
           cursor="hand2", fg=buttonColor, padx=8, pady=5, command=prepareFile).place(x=590, y=298)
    # Inputs
    input_text1 = Text(root, width=92, height=8, bg=textBackgroundColor, fg=textColor)
    input_text1.place(x=20, y=160)

    input_text2 = Text(root, width=45, height=18, bg=textBackgroundColor, fg=textColor)
    input_text2.place(x=20, y=400)

    input_text3 = Text(root, width=45, height=18, bg=textBackgroundColor, fg=textColor)
    input_text3.place(x=400, y=400)

    # Start the main loop
    root.mainloop()
    sys.exit(0)


def lookForFile():
    """
    Opens a file dialog to select a Python (.py) file, reads its content,
    and displays it in the source code input area.
    """
    global filename
    global input_text1
    filename = tk.filedialog.askopenfilename()
    try:
        if filename.endswith(".py"):
            delete_empty_lines_at_end()
            file = open(filename, 'r')
            code = file.read()
            file.close()
            input_text1.delete('1.0', END)
            input_text1.insert(END, code)
        elif filename:
            tk.messagebox.showwarning("Error", "A .py file must be chosen")
            lookForFile()
    except Exception as e:
        pass


def prepareFile():
    global filename
    global input_text1
    filename = "./input.py"
    # Writes the content of the source code input area to a file named 'input.py'.
    input_text2.delete('1.0', END)
    input_text3.delete('1.0', END)
    input_text0 = ""
    fileWrite = open('graph.txt', 'w')
    fileWrite.write(input_text0)
    fileWrite.close()
    delete_empty_lines_from_text()
    fileWrite = open('input.py', 'w')
    fileWrite.write(input_text1.get("1.0", END))
    fileWrite.close()
    return filename


def eraseCode():
    # Clears the content of the source code input area.
    global input_text1
    input_text1.delete('1.0', END)


def delete_empty_lines_at_end():
    global filename
    # Read the content of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Find the index of the last non-empty line
    last_non_empty_index = len(lines) - 1
    while last_non_empty_index >= 0 and lines[last_non_empty_index].strip() == "":
        last_non_empty_index -= 1

    # Truncate the file up to the last non-empty line
    with open(filename, 'w') as file:
        file.writelines(lines[:last_non_empty_index + 1])


def delete_empty_lines_from_text():
    # Get text from the text area
    text_content = input_text1.get("1.0", tk.END)

    # Delete empty lines from the end of the text
    lines = text_content.split('\n')
    while lines and not lines[-1].strip():
        lines.pop()
    updated_text_content = '\n'.join(lines)

    # Update the text area with the edited text
    input_text1.delete("1.0", tk.END)
    input_text1.insert(END, updated_text_content)


def executeLexical():
    """
    Executes the lexical analysis using the main function from the 'lexical' module
    and displays the result in the lexical analysis output area.
    """
    global input_text2
    text = lx.main()
    input_text2.delete('1.0', END)
    input_text2.insert(END, text)


def executeSyntax():
    """
    Executes the syntax analysis using the main function from the 'syntax' module
    and displays the result in the syntax analysis output area.
    """
    global input_text3
    text = sy.main()
    input_text3.delete('1.0', END)
    input_text3.insert(END, text)


def restart_application():
    # Destroy the current Tkinter window
    root.destroy()
    # Create a new Tkinter window
    main()


def visual():
    url = "http://www.webgraphviz.com/"
    webbrowser.open(url)


if __name__ == '__main__':
    main()
