### pour les test ###

import tkinter as tk 
from tkinter import ttk




def tes():
    pass

root = tk.Tk()

root.title("Talk with madeline !")

window_width = 650
window_height = 300

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)
root.iconbitmap('./Assets/favicon.ico')



exit_button=ttk.Button(
	root,
	text='Exit',
	command=lambda:	root.quit()
)

exit_button.pack(
	ipadx=5,
	ipady=5,
	expand=True
)


root.mainloop()