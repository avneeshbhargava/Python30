class cal():
    def __init__(self , a , b):
       self.a = a
       self.b = b
    def Add(self , x , y):
        return self.a + self.b
  #      print(x + y)
    def subtract_fun(self, a , b):
         return self.a - self.b
    def divide_function(self, a , b):
         return self.a / self.b
    def multiply_function(self, a , b):
         return self.a * self.b

add = cal(2,3)
print(add.Add(2,3))
print(add.subtract_fun(4,5))
print(add.divide_function(6,3))
print(add.multiply_function(8,9))
