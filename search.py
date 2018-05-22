list=[10,15,20,23,24,78,65]

target=int(input("Enter the value to search:"))

if target in list:
  
  print("yes target available at index:",list.index(target))

else:
  
  print (target,"not available")
