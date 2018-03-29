def reverse(num):
  rev = 0
  while num > 0:
    rev = (10*rev) + num%10
    num //= 10
  return rev
print reverse(67)



