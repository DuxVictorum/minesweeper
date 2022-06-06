from tkinter import *

root = Tk()

# Override the default window settings
root.configure(bg="burlywood")
root.geometry('1200x600')
root.resizable(False, False)
root.title('Amazing Stuff!')

top_frame = Frame(root, bg="sea green", width=1200, height=150)
top_frame.place(x=0, y=0)   # Start the top frame from the upper left corner

# Practice button using Frame()
# mid_frame = Frame(root, bg="gold2", width=40, height=40)
# mid_frame.place(x=580, y=50)

# Run the game window
root.mainloop()
