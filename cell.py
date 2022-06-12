from tkinter import Button

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
    btn = Button(location, width=10, height=4, text=f"{self.x},{self.y}")
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
    pass

  def __repr__(self):
    return f"Cell({self.x}, {self.y})"