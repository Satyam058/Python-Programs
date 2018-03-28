class A:
  def printing(self):
    print("bangalore")
class B:
  def display(self):
    print("delhi")
class C(A,B):
  pass
f1 = C()
f1.printing()
f1.display()
