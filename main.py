from tkinter import *
from turtle import left
import settings
from utils import *
from cell import Cell

root = Tk()

# Override the default window settings
root.configure(bg="grey10")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False, False)
root.title('Amazing Stuff!')

# Top bar
top_frame = Frame(root, bg="grey10", width=width_pct(100), height=height_pct(25))
top_frame.place(x=0, y=0)   # Start the top frame from the upper left corner

# Left sidebar
left_frame = Frame(root, bg="grey10", width=width_pct(25), height=height_pct(75))
left_frame.place(x=0, y=height_pct(25))

# Center frame
center_frame = Frame(root, bg="grey10", width=width_pct(75), height=height_pct(75))
center_frame.place(x=width_pct(25), y=height_pct(25))

# Cells to click on - sample only
# c1 = Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(column=0, row=0)

# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.grid(column=20, row=0)

# Populate basic grid
for x in range(5):
  for y in range(5):
    c = Cell()
    c.create_btn_object(center_frame)
    c.cell_btn_object.grid(column=x, row=y)


# Run the game window
root.mainloop()
