"""Write an object-oriented GUI program that calculates a car’s gas mileage. The program’s window should have Entry
widgets that let the user enter the number of gallons of gas the car holds, and the number of miles it can be driven on
a full tank. When a Calculate MPG button is clicked, the program should display the number of miles that the car may be
driven per gallon of gas. Use the following formula to calculate miles per gallon:  MPG = miles / gallons"""

import tkinter


class MPG:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # top frame

        self.prompt_gallons = tkinter.Label(self.top_frame, text=" Enter how many gallons yours cars holds: ")
        self.gallon_entry = tkinter.Entry(self.top_frame, width=15)

        # pack label
        self.prompt_gallons.pack(side="left")
        self.gallon_entry.pack(side="right")

        # Create label for milage
        self.miles_prompt = tkinter.Label(self.middle_frame, text="How many miles have you traveled? ")
        self.miles_entry = tkinter.Entry(self.middle_frame, width=15)
        # pack
        self.miles_prompt.pack(side="left")
        self.miles_entry.pack(side="left")

        # create widgets for answer
        self.value = tkinter.StringVar()
        self.results_label = tkinter.Label(self.bottom_frame, textvariable=self.value)
        self.calc_button = tkinter.Button(self.bottom_frame, text="Calculate", command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # pack
        self.results_label.pack(side="top")
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # start mainloop
        tkinter.mainloop()

    def calculate(self):
        gas = float(self.gallon_entry.get())
        miles = float(self.miles_entry.get())

        mpg = "Converted to " + format(miles/gas, ",.2f") + " miles per gallons:"
        self.value.set(mpg)


car = MPG()
