import math

class Vector:
  def __init__(self, x, y, z=None, *args):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
      raise ValueError("X and Y coordinates must be 'int' or 'float'")
    self.x = x
    self.y = y
    self.z = z
      
  def __str__(self):
    return f"{type(self).__name__}(x={self.x}, y={self.y}{f', z={self.z}' if self.z else ''})"

  def __add__(self, other):
    if not type(self) == type(other):
      raise ValueError("Given types are different!")
    if (self.z and other.z) or (not self.z and not other.z):
      return Vector(self.x + other.x, self.y + other.y, self.z + other.z if self.z != None and other.z != None else None)
    raise ValueError("Two vectors must be equal coordinate types")
  
  def __sub__(self, other):
    if not type(self) == type(other):
      raise ValueError("Given types are different!")
    z_line = None
    if self.z != None and other.z != None:
      z_line = self.z - other.z if self.z - other.z >= 0 else (self.z - other.z)*-1
    if (self.z and other.z) or (not self.z and not other.z):
      return Vector(self.x - other.x if self.x - other.x >= 0 else (self.x - other.x)*-1, self.y - other.y if self.y - other.y >= 0 else (self.y - other.y)*-1, z_line)
    raise ValueError("Two vectors must be equal coordinate types")

  def __mul__(self, other):
    if not type(self) == type(other):
      raise ValueError("Given types are different!")
    if (self.z and other.z) or (not self.z and not other.z):
      return sum([self.x * other.x, self.y * other.y, self.z * other.z if getattr(self, 'z') and getattr(other, "z") else 0])
    raise ValueError("Two vectors must be equal coordinate types")

  def __rmul__(self, num: int | float):
    if not isinstance(num, (int, float)):
      raise ValueError("Given argument is not an 'int' or 'float' type")
    return Vector(self.x * num, self.y * num, self.z * num if self.z else None)

  def magnitude(self):
    return math.sqrt(self.x**2 + self.y**2 + (self.z**2 if self != None else 0))

  def normalize(self):
    try:
      return Vector(float(f"{self.x / self.magnitude():.3f}"), float(f"{self.y / self.magnitude():.3f}"), float(f"{self.z / self.magnitude():.3f}") if self.z != None else None)
    except ZeroDivisionError:
      return "Magnitude is 0"
    

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
print(v1 + v2, v1-v2, v1*v2, 3*v1, v1.magnitude(), v1.normalize())