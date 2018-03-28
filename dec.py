def attach(func):
       func.data = 3
       return func
 
@attach
def sub (x, y):
       return x - y

print(sub(5, 3))
 
print(sub.data)
