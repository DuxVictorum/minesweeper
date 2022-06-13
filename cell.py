from tkinter import Button
import random
import settings

class Cell:
  all = []
  
  def __init__(self, x, y, is_mine=False):
    self.is_mine = is_mine
    self.x = x
    self.y = y
    self.cell_btn_object = None

    # Append the object to the Cell.all list
    Cell.all.append(self)

  def create_btn_object(self, location):
    btn = Button(location, width=8, height=3, text="M")
    btn.bind('<Button-1>', self.left_click_actions)
    btn.bind('<Button-3>', self.right_click_actions)
    self.cell_btn_object = btn

  def left_click_actions(self, event):
    print(event)
    print("I was left-clicked!")

  def right_click_actions(self, event):
    print(event)
    print("Righty tighties!")

  # Seed the mines
  @staticmethod
  def randomize_mines():
    mined_cells = random.sample(Cell.all, MINES_COUNT)
    for mine in mined_cells:
      mine.is_mine = True

  def __repr__(self):
    return f"Cell({self.x}, {self.y})"