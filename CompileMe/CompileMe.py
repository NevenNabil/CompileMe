# Import the tkinter module to create a GUI (Graphical User Interface).
from tkinter import *
# Import sys and os for system-related functionalities.
import sys
import os
# Import specific functions from the tkinter library for file dialog and message box.
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
# Import the tkinter module with an alias 'tk' for convenience.
import tkinter as tk
# Import custom modules syntax.py and lexical.py for additional functionality.
import syntax as sy
import lexical as lx

# Define global variables to be used across functions or parts of the program.
global input_text1  # Placeholder for a Tkinter text widget or related input field.
global input_text2  # Placeholder for another Tkinter text widget or related input field.
global input_text3  # Placeholder for yet another Tkinter text widget or related input field.
global filename  # Placeholder for storing the name of the current file.


# These global variables may be utilized to store and access information across different parts of the program.
def main():
    global input_text1
    global input_text2
    global input_text3

    # Parent window declaration and configuration
    w = 1000
    h = 720
    root = Tk()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2) - 15
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root.title("CompileMe")

    root.configure(background="#E4F1FF")
    root.resizable(0, 990)

    # Labels
    Label(root, text="CompileMe", font=("Arial", 25), bg="#E4F1FF", fg="#053B50").place(x=420, y=20)
    Label(root, text="Lexical and Syntax Analyzer(PYTHON)", font=("Arial", 10), bg="#E4F1FF", fg="#776B5D").place(x=592,
                                                                                                                  y=33)

    Label(root, text="SOURCE CODE", bg="#E4F1FF", fg="#053B50").place(x=20, y=130)
    Label(root, text="LEXICAL ANALYSIS", bg="#E4F1FF", fg="#053B50").place(x=20, y=375)
    Label(root, text="SYNTAX ANALYSIS", bg="#E4F1FF", fg="#053B50").place(x=515, y=375)

    # Buttons
    import_button = Button(root, text="Import file (.py)", bg="#176B87", cursor="hand2", fg="white", borderwidth='10',
                           command=lookForFile)
    import_button.place(x=20, y=70)

    delete_button = Button(root, text="Delete", cursor="hand2", bg="#952323", fg="white", command=eraseCode)
    delete_button.place(x=900, y=240)

    lexico_analysis_button = Button(root, text="Lexical analysis", bg="#176B87", cursor="hand2", fg="white",
                                    borderwidth='10', command=executeLexicon)
    lexico_analysis_button.place(x=20, y=320)

    syntactic_analysis_button = Button(root, text="Syntax Analysis", bg="#176B87", cursor="hand2", fg="white",
                                       borderwidth='10', command=executeSyntax)
    syntactic_analysis_button.place(x=515, y=320)

    prepare_button = Button(root, text="Prepare Code", bg="#176B87", cursor="hand2", fg="white", borderwidth='10',
                            command=prepareFile)
    prepare_button.place(x=875, y=180)

    # Inputs
    input_text1 = Text(root, width=105, height=8)
    input_text1.place(x=20, y=160)

    input_text2 = Text(root, width=58, height=18)
    input_text2.place(x=20, y=400)

    input_text3 = Text(root, width=58, height=18)
    input_text3.place(x=515, y=400)

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

    """
    Writes the content of the source code input area to a file named 'input.py'.
    """
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
    """
    Clears the content of the source code input area.
    """
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


def executeSyntax():
    """
    Executes the syntax analysis using the main function from the 'syntax' module
    and displays the result in the syntax analysis output area.
    """
    global input_text3
    text = sy.main()
    input_text3.delete('1.0', END)
    input_text3.insert(END, text)


def executeLexicon():
    """
    Executes the lexical analysis using the main function from the 'lexical' module
    and displays the result in the lexical analysis output area.
    """
    global input_text2
    text = lx.main()

    input_text2.delete('1.0', END)
    input_text2.insert(END, text)


if __name__ == '__main__':
    main()
