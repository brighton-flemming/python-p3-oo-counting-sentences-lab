#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
     if not isinstance(value, str):
          print("The value must be a string.")
          self._value = None
     elif value == "":
           print("The value must be a string.")
           self._value = None
     else:
          self._value = value

  def __str__(self) -> str:
        pass
        
     
         



  def is_sentence():
     pass
  
try:
    my_instance = MyString()
    print(my_instance._value)

    my_instance = MyString("Hello, world!")
    print(my_instance._value)

    invalid_instance = MyString(42) 
except ValueError as e:
    print(e) 


 
