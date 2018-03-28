def generators():
  yield 1
  yield 2
  yield 3
  yield 4

x = generators()
print(x.next());
print(x.next());
print(x.next());
print(x.next());
