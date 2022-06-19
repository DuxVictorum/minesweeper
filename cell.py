from tkinter import Button, Label
import random
import settings

class Cell:
  all = []
  cell_count = settings.CELL_COUNT
  cell_count_label_object = None
  
  def __init__(self, x, y, is_mine=False):
    self.is_mine = is_mine
    self.x = x
    self.y = y
    self.cell_btn_object = None

    # Append the object to the Cell.all list
    Cell.all.append(self)

  def create_btn_object(self, location):
    btn = Button(location, width=8, height=3, text="???")
    btn.bind('<Button-1>', self.left_click_actions)
    btn.bind('<Button-3>', self.right_click_actions)
    self.cell_btn_object = btn

  @staticmethod
  def create_cell_count_label(location):
    cell_count_label = Label(
      location, bg='grey10', fg='white',
      text=f"Cells Left: {settings.CELL_COUNT}",
      font=("", 30), width=12, height=4)
    Cell.cell_count_label_object = cell_count_label

  def left_click_actions(self, event):
    if self.is_mine:
      self.show_mine()
    else:
      if self.surrounding_cells_mines == 0:
        for cell_obj in self.surrounding_cells:
          cell_obj.show_cell()
      self.show_cell()

  def get_cell_by_axis(self, x, y):
  # return a cell object based on its x and y values
    for cell in Cell.all:
      if cell.x == x and cell.y == y:
        return cell

  @property
  def surrounding_cells(self):
    neighbor_cells = [
      self.get_cell_by_axis(self.x-1, self.y-1),
      self.get_cell_by_axis(self.x-1, self.y),
      self.get_cell_by_axis(self.x-1, self.y+1),
      self.get_cell_by_axis(self.x, self.y-1),
      self.get_cell_by_axis(self.x, self.y+1),
      self.get_cell_by_axis(self.x+1, self.y-1),
      self.get_cell_by_axis(self.x+1, self.y),
      self.get_cell_by_axis(self.x+1, self.y+1)
    ]
    # Remove cells off the map
    neighbor_cells = [cell for cell in neighbor_cells if cell is not None]
    return neighbor_cells

  @property
  def surrounding_cells_mines(self):
    counter = 0
    for cell in self.surrounding_cells:
      if cell.is_mine:
        counter += 1
    return counter

  def show_mine(self):
    # Interrupt game and display "You Lost" message
    self.cell_btn_object.configure(bg='red', text='Boom!')

  def show_cell(self):
    Cell.cell_count -= 1
    self.cell_btn_object.configure(text=self.surrounding_cells_mines)
    # Replace the text of 'cell count' label with the updated count


  def right_click_actions(self, event):
    if self.is_mine:
      self.show_mine()


  # Seed the mines
  @staticmethod
  def randomize_mines():
    mined_cells = random.sample(Cell.all, settings.MINES_COUNT)
    for mine in mined_cells:
      mine.is_mine = True

  def __repr__(self):
    return f"Cell({self.x}, {self.y})"