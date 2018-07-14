As the [official Python documentation](https://docs.python.org/2/library/functions.html#super) says:


“[Super is used to] return a proxy object that delegates method calls to a parent or sibling class of type. 
This is useful for accessing inherited methods that have been overridden in a class. 
The search order is same as that used by getattr() except that the type itself is skipped.”


Use case in Python3: 
class MyParentClass():
  def __init__(self, x, y):
  pass

class SubClass(MyParentClass):
  def __init__(self, x, y):
    super().__init__(x, y)
