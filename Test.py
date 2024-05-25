import tkinter as tk
from tkinter import ttk
import Name_List_Selection


window = tk.Tk()
window.title("Test")
window.geometry("600x400")

window.columnconfigure(0 ,weight=1, uniform='a')
window.rowconfigure(0 ,weight=1, uniform='a')

main_frame = ttk.Frame(window, borderwidth=5, relief='groove')
main_frame.grid(column=0, row=0, sticky='nsew')

name_list = Name_List_Selection.select_for(batch='CLASS_11_B3')
num_of_reports = len(name_list)
main_frame_row_list = []
'''Layout in Canvas'''
for i in range(num_of_reports):
    main_frame_row_list.append(i)

main_frame.columnconfigure(0, weight=1, uniform='b')
main_frame.columnconfigure(main_frame_row_list, weight=1, uniform='b')

individual_frames = []

for i in range(0, num_of_reports):
    frame = ttk.Frame(main_frame, borderwidth=5, relief='groove')
    frame.propagate(False)
    frame_label = ttk.Label(frame, text=f"Label {i}", font='comicsans 18')
    frame_label.pack()
    frame.grid(column=0, row=i, sticky='nsew', pady=10)



window.mainloop()