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

        

    def is_sentence(self):
      if self._value is None:
         return False
      return self._value.endswith(".")
  
    def is_question(self):
       if self._value is None:
          return False
       return self._value.endswith("?")
  
    def is_exclamation(self):
      if self._value is None:
          return False
      return self._value.endswith("!")
  
    def count_sentences(self):
      if self._value is None:
       return 0
     
      import re
      sentences = re.split(r'[.!?]', self._value)
      sentences = [s.strip() for s in sentences if s.strip()]
   
      return( len(sentences) )
 

  
  
my_instance1 = MyString()
print(my_instance1._value)
print(my_instance1.count_sentences())

my_instance2 = MyString("What's up?")
print(my_instance2._value)
print(my_instance2.count_sentences())

my_instance3 = MyString("Hi.")
print(my_instance3._value)
print(my_instance3.count_sentences())

my_instance4 = MyString("one. two. three?")
print(my_instance4._value)
print(my_instance4.count_sentences())

my_instance5 = MyString("Hello, world!")
print(my_instance5._value)
print(my_instance5.count_sentences())

my_instance6 = MyString("This is the first sentence. The second sentence follows. Now we have a third sentence! Finally, the fourth sentence concludes the text.")
print(my_instance6._value)
print(my_instance6.count_sentences())

my_instance7 = MyString("Here comes the first sentence. The second sentence is right behind. Sentence number three is right here. The fourth sentence arrives. And lastly, the fifth sentence concludes everything!")
print(my_instance7._value)
print(my_instance7.count_sentences())

invalid_instance = MyString(42) 
print(invalid_instance._value)
print(invalid_instance.count_sentences())


  


 
