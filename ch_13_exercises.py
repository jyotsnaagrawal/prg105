"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)


# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2
class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        tkinter.mainloop()


if __name__ == '__main__':
    mygui2 = MyGUI2()

# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)


# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2
class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Jyotsna Agrawal')
        tkinter.mainloop()


if __name__ == '__main__':
    mygui2 = MyGUI2()

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)


# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3
class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Jyotsna-Mobile Application and development')
        self.label1.pack()
        self.label2 = tkinter.Label(self.bottom_frame, text='PRG-105')
        self.label2.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


if __name__ == '__main__':
    mygui3 = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)


# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI
class JokeGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.joke_label = tkinter.Label(self.top_frame, text='Why does Waldo wear stripes?')
        self.joke_label.pack()
        self.answer_button = tkinter.Button(self.bottom_frame, text='Answer', command=self.show_answer)
        self.answer_button.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    @staticmethod
    def show_answer():
        tkinter.messagebox.showinfo('Answer', 'Because he does not want to be spotted.')


joke = JokeGUI()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)


# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


class Converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text="Enter size in inches")
        self.prompt_label.pack()
        self.inches_entry = tkinter.Entry(self.top_frame, width=6)
        self.inches_entry.pack()

        self.convert_button = tkinter.Button(self.bottom_frame, text="CONVERT", command=self.convert)
        self.convert_button.pack(side="left")
        self.quit_button = tkinter.Button(self.bottom_frame, text="QUIT", command=self.main_window.destroy)
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        inches = float(self.inches_entry.get())
        centimeters = inches * 2.54
        tkinter.messagebox.showinfo("Results", str(inches) + "inches equals " + str(centimeters) + "centimeters.")


convert_gui = Converter()

