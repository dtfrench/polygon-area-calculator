class Rectangle:

  def __init__(self, width, height):

    self.width = width
    self.height = height
  
  def __str__(self):

    rec_str =f"Rectangle(width={self.width}, height={self.height})"
    return rec_str
  
  def set_width(self, width):

    self.width = width
  
  def set_height(self, height):

    self.height = height
  
  def get_area(self):

    area = self.width * self.height
    return area
  
  def get_perimeter(self):

    perimeter = 2 * self.width + 2 * self.height
    return perimeter
  
  def get_diagonal(self):

    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal
  
  def get_picture(self):

    if (self.width > 50 or self.height > 50):
      return "Too big for picture."

    pic_string = ''
    for num in range(self.height):
      for num in range(self.width):

        pic_string += '*'
      pic_string += '\n'

    return pic_string
  
  def get_amount_inside(self, shape):

    times_fit = 0

    if (shape.height > self.height or shape.width > self.width):
      times_fit = 0
    
    elif (shape.height < self.height or shape.width < self.width):
      width_num = self.width / shape.width
      if (type(width_num) != int):
        width_num = int(width_num)
      
      height_num = self.height / shape.height 
      if (type(height_num) != int):
        height_num = int(height_num)

      times_fit = width_num * height_num 
    
    else:
      times_fit = 1

    print(times_fit)
    return times_fit

class Square(Rectangle):

  def __init__(self, side):
     self.width = side
     self.height = side
    
  def __str__(self):
    side_str =f"Square(side={self.width})"
    return side_str
  
  def set_side(self, side):
    self.width = side
    self.height = side
    
    

    
    
  
  

   

    

