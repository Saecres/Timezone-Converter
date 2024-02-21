# Name: Kaitlin Penaranda
# Date: November 22, 2022
# App Name: Canadian Time Zones
# Description: App that shows time in different Canadian time zones

from tkinter import *                           # Import the tkinter module
from tkinter.ttk import *                       # replaces the w95 look with modern one
from datetime import datetime, timedelta        # UTC

# Constants
TIMEZONE_NAMES = ("Pacific Time", "Mountain Time", "Central Time", "Eastern Time", "Atlantic Time", "Newfoundland TIme")
TIME_SHIFT = (-8,-7,-6,-5,-4,-3)    # Time difference from UTC

# Defining functions
def get_time():
    """Gets the current time in the selected timezone"""

    # Get the DST selection from the checkbox
    dst = int(dst_selection.get())                      # convert to 0 or 1

    # Get the current selected timezone from the combobox
    # Get index from time shift to know how many hours to shift
    time_zone = TIME_SHIFT[timezones_combobox.current()]

    # Shift time
    date_time = datetime.utcnow() + timedelta(hours=time_zone + dst)

    # Display the time
    time_format = "%I:%M :%p"                       # hour:minute AM/PM
    date_string = date_time.strftime(time_format)   
    
    # Return the time as a str
    return date_string

def showtime_click():
    """Update the time"""
    output_text.set(get_time())

def clear_click():
    # resets combobox to est
    timezone_selection.set(TIMEZONE_NAMES[3])
    # resets checkbox to unchecked
    dst_selection.set(False)
    # Updates the time
    showtime_click()

# Setup the window
window = Tk()
window.title("Canadian Time Zones - Kaitlin Penaranda")
window.iconbitmap("Canada.ico")
window.resizable(width=False, height=False)     # WIndow is not resizable

# Frames
input_frame = Frame()
output_frame = Frame()

# Labels
input_label = Label(input_frame, text="Select a time zone:")

# Combobox
timezone_selection = Variable()                                 # Tkinter variable for widgets
timezone_selection.set(TIMEZONE_NAMES[3])                       # index 3 of tuple
#                                                 options           currently selected timezone
timezones_combobox = Combobox(input_frame, values=TIMEZONE_NAMES, textvariable=timezone_selection, state="readonly")

# Checkbutton
dst_selection = Variable()
dst_selection.set(False)
dst_checkbutton = Checkbutton(input_frame, text="Daylight Saving Time", variable=dst_selection)

# Buttons
show_time_button = Button(input_frame, text="Show Time", command=showtime_click)
clear_button = Button(input_frame, text="Clear", command=clear_click)

# Place widgets
# Input
input_frame.pack(padx=10, pady=10, side="left")      # Padding of 10px around frame
input_label.pack(anchor="w")            # Anchor to west (left)
timezones_combobox.pack(anchor="w")
dst_checkbutton.pack(anchor="w")
show_time_button.pack(side="right")
clear_button.pack(side="left")

output_text = Variable()
output_text.set(get_time())
output_label = Label(output_frame, textvariable=output_text, font="Consolas 45")

# Output
output_frame.pack(padx=10, pady=10, side="right")   # padding of 10px around frame
output_label.pack()

# Show the window
window.mainloop()