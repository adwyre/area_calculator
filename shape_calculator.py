class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height
  def get_area(self):
    return (self.width * self.height)
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    picture = ""
    i = 0
    while i < self.height:
      j = 0
      while j < self.width:
        picture += "*"
        j += 1
      picture += "\n"
      i += 1
    return picture
  def get_amount_inside(self, shape):
    area1 = self.get_area()
    area2 = shape.get_area()
    if area2 > area1:
      return 0
    return int(area1/area2)

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
  def __str__(self):
    return "Square(side=" + str(self.width) + ")"
  def set_side(self, side):
    self.width = side
    self.height = side
