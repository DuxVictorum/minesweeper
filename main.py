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

game_title = Label(top_frame, bg='grey10', fg='white', text='Minesweeper Game', font=('', 48))
game_title.place(x=width_pct(25), y=20)

# Left sidebar
left_frame = Frame(root, bg="grey10", width=width_pct(25), height=height_pct(75))
left_frame.place(x=0, y=height_pct(25))

# Center frame
center_frame = Frame(root, bg="grey10", width=width_pct(75), height=height_pct(75))
center_frame.place(x=width_pct(25), y=height_pct(25))

# Populate basic grid
for x in range(settings.GRID_SIZE):
  for y in range(settings.GRID_SIZE):
    c = Cell(x, y)
    c.create_btn_object(center_frame)
    c.cell_btn_object.grid(column=x, row=y)

# Call label for Left Frame from Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()


# Run the game window
root.mainloop()
