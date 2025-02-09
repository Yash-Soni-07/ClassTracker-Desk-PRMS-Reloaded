import tkinter as tk
from tkcalendar import DateEntry

def get_date():
    selected_date = date_entry.get_date()  # Get selected date as a datetime object
    formatted_date = selected_date.strftime("%Y_%B_%d")  # Format as YYYY_MONTH_DD
    print("Selected Date:", formatted_date)

# Create main window
root = tk.Tk()
root.title("Date Picker Example")

# Create Date Picker
tk.Label(root, text="Select Date:").pack(pady=5)
date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="yyyy/mm/dd")
date_entry.pack(pady=5)

# Button to fetch and format selected date
btn = tk.Button(root, text="Get Date", command=get_date)
btn.pack(pady=10)

# Run the application
root.mainloop()
