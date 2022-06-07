from tkinter import *
from turtle import left
import settings

root = Tk()

# Override the default window settings
root.configure(bg="burlywood")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False, False)
root.title('Amazing Stuff!')

# Top bar
top_frame = Frame(root, bg="sea green", width=1200, height=150)
top_frame.place(x=0, y=0)   # Start the top frame from the upper left corner

# Practice button using Frame()
# mid_frame = Frame(root, bg="gold2", width=40, height=40)
# mid_frame.place(x=580, y=50)

# Left sidebar
left_frame = Frame(root, bg="blue", width=300, height=450)
left_frame.place(x=0, y=150)

# Run the game window
root.mainloop()
